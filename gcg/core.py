import datetime
import json
import os
import uuid
from collections import namedtuple

import boto3
import jinja2
from gcg.env import TEMPLATE_FOLDER, AWS_SECRET_KEY, AWS_ACCESS_KEY, TEMP_FOLDER
from gcg.exceptions import GCGValidationError
from gcg.maps import MAP_TEMPLATE_TYPES
from gcg.utils import make_file_path
from gcg.log import gcg_logger

from marshmallow import Schema, fields
from marshmallow.validate import OneOf

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, TEMPLATE_FOLDER)

templateLoader = jinja2.FileSystemLoader(searchpath=[path])
templateEnv = jinja2.Environment(loader=templateLoader, trim_blocks=True, lstrip_blocks=True, autoescape=True)


class GeneratorTaskSchema(Schema):
    template_type = fields.String(required=True, validate=OneOf(list(MAP_TEMPLATE_TYPES.keys())))
    data = fields.Dict(required=True)


GenesisResults = namedtuple('GenesisResults', ['task_completed', 'task_remaining'])


class Task:
    """
    This object represents a Single Configuration Generation task. This object allows the GCG to
    validate the configuration schema and data. The GCG will execute each configuration task to output the
    desired results.


    Supports the following Data structure:

      task = Task(
        data=data,
        template_type=template_type,
        name=name,
        description=description
    )

    """

    def __init__(self, **kwargs):

        self.data = kwargs.get("data")
        if kwargs.get("name") is None:
            self.name = str(uuid.uuid4())
        else:
            self.name = kwargs.get("name")

        self.description = kwargs.get("description")

        self.rendered_data = None
        self.is_complete = False
        self.template_type = kwargs.get("template_type")
        #
        self._schema = None
        self._template_file_name = None

        self._set_template_type(self.template_type)

    def _set_template_type(self, template_type: str):
        """
        Set the current template type of the object.
        """
        MAP_RESULTS = MAP_TEMPLATE_TYPES.get(template_type)

        if MAP_RESULTS is None:
            raise GCGValidationError(
                f"Invalid Template Type provide'{template_type}', Choices: {MAP_TEMPLATE_TYPES.keys()}")
        else:
            self.template_type = template_type
            self._schema = MAP_RESULTS.get("schema")
            self._template_file_name = MAP_RESULTS.get("template_file")
            return True

    def validate(self):
        """
        Validates the data stored in Task object based on the template_type schema.

        returns True is successful else return False
        """
        if self._schema:
            if len(self._schema.validate(self.data)) > 0:
                raise GCGValidationError(self._schema.validate(self.data))

            return True

    def validate_data(self, data):
        """
        Validates the data provided. This allows the user to validate additional data structures before setting
        the data in GeneratorTask object.

        """
        if self._schema:
            if len(self._schema.validate(data)) > 0:
                raise GCGValidationError(self._schema.validate(data))
            else:
                return True

    def __repr__(self):
        return f'<Task(template_type={self.template_type}, name={self.name}, description={self.description})>'

    @staticmethod
    def list_template_types():
        """
        Returns a list of available template types.
        """
        return list(MAP_TEMPLATE_TYPES.keys())


class Genesis:
    """
    ConfigGenerator is the main class that will ge

    """

    def __init__(self, **kwargs):
        self.tasks = kwargs.get("tasks", [])
        self.task_completed = []
        self.task_remaining = []

    def add_task(self, task: Task) -> bool:
        """
        Adds new task to the tasks list. If the task is not an instances of GeneratorTask,
        return False.

        """
        if isinstance(task, Task):
            gcg_logger.debug(f'Appended {task} to {self}')
            self.tasks.append(task)
            return True
        else:
            raise TypeError(f'Invalid Type, Must be instance of type: {Task}')

    def generate(self, store_aws=False, store_local=False, **kwargs) -> GenesisResults:
        """
        Iterates through the list of tasks and generates the requested configurations. If the configuration generation
        was completed successfully, CGC sets each task.is_complete to true.

        """
        save_location = kwargs.get("save_location")

        for task in self.tasks:
            self.generate_config_from_task(
                task=task,
                store_aws=store_aws,
                store_local=store_local,
                save_location=save_location
            )


        for task in self.tasks:
            if task.is_complete:
                self.task_completed.append(task)
            else:
                self.task_remaining.append(task)

        return GenesisResults(task_completed=self.task_completed, task_remaining=self.task_remaining)

    @staticmethod
    def generate_config_from_task(task: Task, store_aws=False, store_local=False, **kwargs) -> GenesisResults:
        """
        Takes the Task object and generates the configuration based on the Task.template_type param.

        Returns the reference of the original Task object.
        """

        LAB_NAME = kwargs.get("lab_name", datetime.datetime.now().strftime("%m_%d_%Y"))
        SAVE_LOCATION = kwargs.get("save_location")

        template_file_name = task._template_file_name
        template_file = _open_template(template_file_name)

        try:
            task.rendered_data = template_file.render(**task.data)
            task.is_complete = True
            gcg_logger.debug(f'Generated "{task.template_type}" Task: {task}')
        except Exception:
            task.is_complete = False
            raise

        if store_aws:
            s3_client = boto3.client('s3',
                                     aws_access_key_id=AWS_ACCESS_KEY,
                                     aws_secret_access_key=AWS_SECRET_KEY
                                     )

            temp_file = f'{TEMP_FOLDER}/{task.name}.txt'
            with open(temp_file, 'w') as f:
                f.write(task.rendered_data)

            s3_client.upload_file(temp_file, 'cbaxter1988', f'gcg_configs/{LAB_NAME}/{task.name}.txt')

            os.remove(temp_file)
            gcg_logger.debug(f'Uploaded {task.name} to AWS S3')

        if store_local:
            save_location = SAVE_LOCATION if SAVE_LOCATION is not None else TEMP_FOLDER

            temp_file = f'{save_location}/{task.name}.txt'

            with open(temp_file, 'w') as f:
                f.write(task.rendered_data)

        if task.is_complete:
            return GenesisResults(task_completed=[task], task_remaining=[])


# Help Functions
def _open_json_file(file_name):
    try:
        with open(file_name, "r") as json_file:
            data = json.load(json_file)
            return data
    except Exception:
        raise


def _open_template(template_name):
    path = make_file_path(__file__, template_name)
    template = templateEnv.get_template(template_name)
    return template


def _write_template(data, template, output_filename) -> bool:
    try:
        with open(output_filename, "w") as f:
            template = template.render(**data)
            f.write(template)
        return True
    except Exception:
        raise
