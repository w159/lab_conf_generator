import json
import jinja2

from lcg.constants import MAP_TEMPLATE_FILES

templateLoader = jinja2.FileSystemLoader(searchpath="../lcg/template")
templateEnv = jinja2.Environment(loader=templateLoader, trim_blocks=True, lstrip_blocks=True)


class ConfigGenerator:
    def __init__(self, **kwargs):
        self._template_opts = MAP_TEMPLATE_FILES.get(kwargs.get("template_file"))

        if self._template_opts is None:
            self.template_file = None
        else:
            self.template_file = self._template_opts.get("template_file")

        self.output_file = kwargs.get("output_file", None)
        self.facts = kwargs.get("facts", None)

        if self.template_file:
            self.template = _open_template(self.template_file)

    def read_json(self, json_file) -> bool:
        try:
            data = _open_json_file(json_file)
            self.facts = data
            return True
        except Exception:
            raise

    def set_template(self, template_type):

        self._template_opts = MAP_TEMPLATE_FILES.get(template_type, None)

        if self._template_opts is None:
            raise Exception(f"Invalid template type, select from:\n {list(MAP_TEMPLATE_FILES.keys())} ")

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
                raise Exception(validation_results)

        except Exception:
            raise

    def to_stdout(self):
        if not self.template:
            raise Exception("Class missing 'template' name")

        if not self.facts:
            raise Exception("Class missing 'facts' name")


        data = self.template.render(**self.facts)

        return data

    def write(self):
        if not self.template:
            raise Exception("Class missing 'template' name")

        if not self.output_file:
            raise Exception("Class missing 'output_file' name")

        schema = self._template_opts.get("schema")

        validation_results = schema.validate(self.facts)
        if len(validation_results.keys()) == 0:

            _write_template(self.facts, self.template, self.output_file)

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
