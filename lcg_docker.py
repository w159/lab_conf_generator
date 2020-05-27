import argparse
import json

from lcg.controllers.config_gen import ConfigGenerator


def ios_base_config(data):
    cg = ConfigGenerator(template_type="ios_rtr")
    cg.set_facts(data)

    print("########################")
    print(f'\t{data.get("hostname")}')
    print("########################")
    print(cg.render())
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
    print(config_gen.render())
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
    parser.add_argument("--config", help="Generates Base Config for router")

    args = parser.parse_args()

    if args.config:
        data = _open_file(args.config)
        if data.get("node_type") == "ios_rtr":
            ios_base_config(data)
            exit(0)

        if data.get("node_type") == "ios_xr":
            xr_base_config(data)
            exit(0)

    parser.print_help()


if __name__ == "__main__":
    main()
