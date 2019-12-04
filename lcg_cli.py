import json
import argparse

from lcg.controllers.config_gen import ConfigGenerator


def _process_ios_base_config(data, out_filename):
    if data['node_type'] == 'ios':
        config_gen = ConfigGenerator(template_type="ios_base_node",
                                     output_file=out_filename,
                                     facts=data
                                     )
        config_gen.write()


def _process_ios_te_tunnels(data, out_filename):
    if data['node_type'] == 'ios':
        config_gen = ConfigGenerator(template_type="ios_te_tunnels",
                                     output_file=out_filename,
                                     facts=data
                                     )
        config_gen.write()


def _process_bgp_policy(data, out_filename):
    if data['node_type'] == 'ios':
        config_gen = ConfigGenerator(template_type="ios_bgp_policy",
                                     output_file=out_filename,
                                     facts=data
                                     )
        config_gen.write()


def _process_bgp_session(data, out_filename):
    if data['node_type'] == 'ios':
        config_gen = ConfigGenerator(template_type="ios_bgp_session",
                                     output_file=out_filename,
                                     facts=data
                                     )
        config_gen.write()


def _open_input_file(file_name):
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

        data = _open_input_file(input_filename)
        _process_ios_base_config(data, output_filename)
        print(f"{data['hostname']} Configuration Generated: {output_filename}.")
        exit()

    if args.te_tunnels:
        input_filename = args.te_tunnels
        data = _open_input_file(input_filename)
        _process_ios_te_tunnels(data, output_filename)
        exit(0)

    if args.bgp_policy:
        input_filename = args.bgp_policy
        data = _open_input_file(input_filename)
        _process_bgp_policy(data, output_filename)
        exit(0)

    if args.bgp_session:
        input_filename = args.bgp_session
        data = _open_input_file(input_filename)
        _process_bgp_session(data, output_filename)
        exit(0)

    print(parser.print_help())


if __name__ == "__main__":
    main()
