import jinja2
import json

templateLoader = jinja2.FileSystemLoader(searchpath="../template")
templateEnv = jinja2.Environment(loader=templateLoader)