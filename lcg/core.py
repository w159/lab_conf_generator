import json
import jinja2
import os
import uuid

import boto3

from marshmallow import Schema, fields
from marshmallow.validate import OneOf

from lcg.maps import MAP_TEMPLATE_TYPES
from lcg.utils import make_file_path
from lcg.exceptions import GCGError, GCGValidationError
from lcg.env import TEMPLATE_FOLDER, AWS_SECRET_KEY, AWS_ACCESS_KEY

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, TEMPLATE_FOLDER)

templateLoader = jinja2.FileSystemLoader(searchpath=[path])
templateEnv = jinja2.Environment(loader=templateLoader, trim_blocks=True, lstrip_blocks=True, autoescape=True)


class GeneratorTaskSchema(Schema):
    template_type = fields.String(required=True, validate=OneOf(list(MAP_TEMPLATE_TYPES.keys())))
    data = fields.Dict(required=True)


class GeneratorTask:
    """
    This object represents a Single Configuration Generation task. This object allows the GCG to
    validate the configuration schema and data. The GCG will execute each configuration task to output the
    desired results.


    Supports the following Data structure:

    {
        template_type: OneOf(MAP_TEMPLATE_TYPES)
        data: {}
    }


    """

    def __init__(self, **kwargs):
        task_schema = GeneratorTaskSchema()
        data = kwargs.get('data')

        self.data = data.get("data")

        self.name = kwargs.get("name", str(uuid.uuid4()))

        self.description = data.get("description", "")

        self.rendered_data = None
        self.is_complete = False
        self.template_type = None

        self._schema = None
        self._template_file_name = None

        self.set_template_type(data.get("template_type"))

    @staticmethod
    def new(name=None, data=None):
        """
        Generates a new GeneratorTask object

        """
        if name is None:
            name = uuid.uuid4()

        return GeneratorTask(name=name, data=data)

    def set_template_type(self, template_type: str):
        """
        Set the current template type of the object.
        """
        MAP_RESULTS = MAP_TEMPLATE_TYPES.get(template_type)

        if MAP_RESULTS is None:
            raise GCGValidationError(f"Invalid Template Type provide, Choices: {MAP_TEMPLATE_TYPES.keys()}")
        else:
            self.template_type = template_type
            self._schema = MAP_RESULTS.get("schema")
            self._template_file_name = MAP_RESULTS.get("template_file")
            return True

    def validate(self):
        """
        Validates the current data stored in object based on the template type schema.

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

    @staticmethod
    def template_types():
        """
        Returns a list of available template types.
        """
        return list(MAP_TEMPLATE_TYPES.keys())


class GCG:
    """
    ConfigGenerator is the main class that will ge

    """

    def __init__(self, **kwargs):
        self.tasks = kwargs.get("tasks", [])

    def add_task(self, task: GeneratorTask) -> bool:
        """
        Adds new task to the tasks list. If the task is not an instances of GeneratorTask,
        return False.

        """
        if isinstance(task, GeneratorTask):
            self.tasks.append(task)
            return True
        else:
            raise TypeError(f'Invalid Type, Must be instance of type: {GeneratorTask}')

    def generate(self, store_aws=False, store_local=False):
        """
        Iterates through the list of tasks and generates the requested configurations. If the configuration generation
        was completed successfully, CGC sets each task.is_complete to true.

        """
        results = {}

        results['task_completed'] = []
        results['task_remaining'] = []

        for task in self.tasks:

            template_file_name = task._template_file_name
            template_file = _open_template(template_file_name)
            try:
                task.rendered_data = template_file.render(**task.data)
                task.is_complete = True
            except Exception:
                task.is_complete = False
                raise

            if store_aws:


                s3_client = boto3.client('s3',
                                         aws_access_key_id=AWS_ACCESS_KEY,
                                         aws_secret_access_key=AWS_SECRET_KEY
                                         )

                temp_file = f'../lcg/.tmp/{task.name}.txt'
                with open(temp_file, 'w') as f:
                    f.write(task.rendered_data)

                s3_client.upload_file(temp_file, 'cbaxter1988', f'gcg_configs/{task.name}.txt')
                os.remove(temp_file)

            if store_local:
                temp_file = f'../lcg/.tmp/{task.name}.txt'
                with open(temp_file, 'w') as f:
                    f.write(task.rendered_data)

        for task in self.tasks:
            if task.is_complete:
                results['task_completed'].append(task)
            else:
                results['task_remaining'].append(task)

        return results


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
