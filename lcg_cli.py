import jinja2
import json
import argparse
from marshmallow import Schema, fields


class BaseConfigSchema(Schema):
    hostname = fields.String()


templateLoader = jinja2.FileSystemLoader(searchpath="./template")
templateEnv = jinja2.Environment(loader=templateLoader, trim_blocks=True, lstrip_blocks=True)


def _write_template(data, template, output_filename):
    with open(output_filename, "w") as f:
        template = template.render(**data)
        f.write(template)
        print(f"\nSuccessfully Generated Template: '{ output_filename }'")


def _process_ios_base_config(data, out_filename):
    TEMPLATE_FILE = "ios_base_config.j2"
    template = templateEnv.get_template(TEMPLATE_FILE)
    _write_template(data, template, out_filename)


def _process_ios_te_tunnels(data, out_filename):
    if data['node_type'] == 'ios':
        TEMPLATE_FILE = "ios_te_tunnel.j2"
        template = templateEnv.get_template(TEMPLATE_FILE)
        _write_template(data, template, out_filename)
        print("Completed")


def _process_bgp_policy(data, out_filename):
    if data['node_type'] == 'ios':
        TEMPLATE_FILE = "ios_bgp_policy.j2"
        template = templateEnv.get_template(TEMPLATE_FILE)
        _write_template(data, template, out_filename)


def _process_bgp_session(data, out_filename):
    if data['node_type'] == 'ios':
        TEMPLATE_FILE = "ios_bgp_session.j2"
        template = templateEnv.get_template(TEMPLATE_FILE)
        _write_template(data, template, out_filename)


def _open_file(file_name):
    with open(file_name, "r") as json_file:
        data = json.load(json_file)
        print(f"Successfully Read JSON Data: '{file_name}'")
        return data


def main():
    parser = argparse.ArgumentParser(description='Byt3m3 Lab Configuration Generator')
    parser.add_argument("--base_config", help="Generates Base Config for router")
    parser.add_argument("--te_tunnels", help="Generates Base Config for router")
    parser.add_argument("--bgp_policy", help="Generates BGP policy-template configurations")
    parser.add_argument("--bgp_session", help="Generates BGP session-template configurations")
    parser.add_argument("-o", help="Output File Name")

    args = parser.parse_args()

    if not args.o:
        try:
            raise Exception("Please provide output filename using the '-o' Flag")
        except Exception as error:
            print(error)
            exit()

    output_filename = args.o

    if args.base_config:
        input_filename = args.base_config

        data = _open_file(input_filename)
        _process_ios_base_config(data, output_filename)
        print(f"{data['hostname']} Configuration Generated: {output_filename}.")
        exit()

    if args.te_tunnels:
        input_filename = args.te_tunnels
        data = _open_file(input_filename)
        _process_ios_te_tunnels(data, output_filename)
        exit(0)

    if args.bgp_policy:
        input_filename = args.bgp_policy
        data = _open_file(input_filename)
        _process_bgp_policy(data, output_filename)
        exit(0)

    if args.bgp_session:
        input_filename = args.bgp_session
        data = _open_file(input_filename)
        _process_bgp_session(data, output_filename)
        exit(0)


    print(parser.print_help())

if __name__ == "__main__":
    main()
