import json
import jinja2

from lcg.constants import MAP_TEMPLATE_FILES

templateLoader = jinja2.FileSystemLoader(searchpath="../lcg/template")
templateEnv = jinja2.Environment(loader=templateLoader, trim_blocks=True, lstrip_blocks=True)


class ConfigGenerator:
    def __init__(self, **kwargs):
        self.template_file = MAP_TEMPLATE_FILES.get(kwargs.get("template_file"), None)
        self.output_file = kwargs.get("output_file")
        self.facts = kwargs.get("facts", None)

        if self.template_file:
            self.template = _open_template(self.template_file)

    def load(self) -> bool:
        """
        Loads the template from the file.

        :return:
        """
        try:
            template_file = MAP_TEMPLATE_FILES.get(self.template_file)

            self.template_file = templateEnv.get_template(template_file)

            return True
        except Exception:
            raise

    def read_json(self, json_file) -> bool:
        try:
            data = _open_json_file(json_file)
            self.facts = data
            return True
        except Exception:
            raise

    def set_template(self, template_type):

        _template_file = MAP_TEMPLATE_FILES.get(template_type, None)

        if _template_file is None:
            raise Exception(f"Invalid template type, select from:\n {list(MAP_TEMPLATE_FILES.keys())} ")

        self.template = _open_template(_template_file)

        self.template_file = _template_file

    def set_output_file(self, file_name) -> bool:
        try:
            self.output_file = file_name
            return True

        except Exception:
            raise

    def set_facts(self, data: dict) -> bool:
        try:
            self.facts = data
            return True

        except Exception:
            raise

    def write(self):
        if not self.template:
            raise Exception()

        _write_template(self.facts, self.template, self.output_file)


# Help Functions
def _open_json_file(file_name):
    try:
        with open(file_name, "r") as json_file:
            data = json.load(json_file)
            return data
    except Exception:
        raise


def _open_template(template_name):
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
