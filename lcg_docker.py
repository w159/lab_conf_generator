import argparse
import json

from lcg.controllers.config_gen import ConfigGenerator


def ios_base_config(data):
    config_gen = ConfigGenerator(template_type="ios_base_node",
                                 facts=data
                                 )

    print("########################")
    print(f'\t{data.get("hostname")}')
    print("########################")
    print(config_gen.to_stdout())
    print("########################")
    print("\tComplete")
    print("########################")


def xr_base_config(data):
    config_gen = ConfigGenerator(template_type="xr_base_config",
                                 facts=data
                                 )

    print("########################")
    print(f'\t{data.get("hostname")}')
    print("########################")
    print(config_gen.to_stdout())
    print("########################")
    print("\tComplete")
    print("########################")


# Utility Functions
def _open_file(file_name):
    with open(file_name, "r") as json_file:
        data = json.load(json_file)
        return data


def main():
    parser = argparse.ArgumentParser(description='Byt3m3 Lab Configuration Generator')
    parser.add_argument("--base_config", help="Generates Base Config for router")

    args = parser.parse_args()

    if args.base_config:
        data = _open_file(args.base_config)
        if data.get("node_type") == "ios":
            ios_base_config(data)
            exit(0)

        if data.get("node_type") == "ios_xr":
            xr_base_config(data)
            exit(0)

    parser.print_help()


if __name__ == "__main__":
    main()
