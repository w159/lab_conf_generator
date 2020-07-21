import json
import jinja2
import os

from lcg.maps import MAP_TEMPLATE_TYPES
from lcg.utils import make_file_path
from lcg.exceptions import LCGSchemaValidationError
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../template")

templateLoader = jinja2.FileSystemLoader(searchpath=[path])
templateEnv = jinja2.Environment(loader=templateLoader, trim_blocks=True, lstrip_blocks=True)


class ConfigGenerator:
    def __init__(self, **kwargs):
        self._template_opts = MAP_TEMPLATE_TYPES.get(kwargs.get("template_type"))

        if self._template_opts is None:
            self.template_file = None
        else:
            self.template_file = self._template_opts.get("template_file")

        self.output_file = kwargs.get("output_file", None)

        self.results = None

        self.facts = kwargs.get("facts", None)

        if self.template_file:
            self.template = _open_template(self.template_file)

    def read_json(self, json_file) -> bool:
        """
            Opens JSON file and stores contents in memory
        """
        try:
            data = _open_json_file(json_file)
            self.facts = data
            return True
        except Exception:
            raise

    def generate(self, data):
        self.set_template(data['template_type'])
        self.set_facts(data)

        return self.render()

    def set_template(self, template_type):

        self._template_opts = MAP_TEMPLATE_TYPES.get(template_type, None)

        if self._template_opts is None:
            raise Exception(f"Invalid template type, select from:\n {list(MAP_TEMPLATE_TYPES.keys())} ")

        template_file = self._template_opts.get("template_file")
        self.template = _open_template(self._template_opts.get("template_file"))
        self.template_file = template_file

    def set_output_file(self, file_name) -> bool:
        try:
            self.output_file = file_name
            return True

        except Exception:
            raise

    def set_facts(self, data: dict) -> bool:
        try:
            schema = self._template_opts.get("schema")

            validation_results = schema.validate(data)
            if len(validation_results.keys()) == 0:
                self.facts = data
                return True

            else:
                raise LCGSchemaValidationError(validation_results)

        except Exception:
            raise

    def render(self):
        """
        Returns String representation of rendered template.

        :return:
        """
        if not self.template:
            raise Exception("Class missing 'template' name")

        if not self.facts:
            raise Exception("Class missing 'facts' name")

        self.results = self.template.render(**self.facts)

        return self

    def write(self):
        if not self.template:
            raise Exception("Class missing 'template' name")

        if not self.output_file:
            raise Exception("Class missing 'output_file' name")

        schema = self._template_opts.get("schema")

        validation_results = schema.validate(self.facts)
        if len(validation_results.keys()) == 0:
            print(self.template)

            # _write_template(self.facts, self.template, self.output_file)

        else:

            raise Exception(validation_results)


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
