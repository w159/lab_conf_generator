import argparse
import json

from gcg.api import app
from gcg.api.controllers.controller_gcg import controller_gcg_v2
from gcg.env import DEBUG, APP_PORT, APP_HOST
from gcg.maps import MAP_TEMPLATE_TYPES


def main():
    parser = argparse.ArgumentParser(
        description='Genesis Configuration Generator',

    )

    cli_arg_group = parser.add_argument_group(
        'Commands for running the GCG CLI tool'
    )

    parser.add_argument(
        '--run',
        action='store_true',
        help="Runs Development HTTP server used to deploy Genesis Configuration Generator"
    )

    cli_arg_group.add_argument(
        '--json',
        help='Specify the JSON file you would like to generate.'
    )
    cli_arg_group.add_argument(
        '--template_type',
        # help='Specify the type of template you would like generated',
        choices=list(MAP_TEMPLATE_TYPES.keys())
    )

    cli_arg_group.add_argument(
        '--store_aws',
        action='store_true',
        help='Flag to store rendered config to AWS'
    )
    cli_arg_group.add_argument(
        '--store_local',
        action='store_true',
        help='Flag to store rendered config to local file system'
    )

    cli_arg_group.add_argument(
        '--aws_access_key',
        help='Access Key used for AWS Boto3 session'
    )
    cli_arg_group.add_argument(
        '--aws_secret_key',
        help='Secret Key used for AWS Boto3 session'
    )

    cli_arg_group.add_argument(
        '--save_location',
        help='Specify location to save the generated config'
    )

    cli_arg_group.add_argument(
        '--config_name',
        help='Specify the name of the Generated configuration .txt file',
    )

    args = parser.parse_args()

    if args.run:
        # Enter Execution Code here
        app.run(debug=DEBUG, port=APP_PORT, host=APP_HOST)

    if args.json:
        json_file = args.json
        save_location = args.save_location

        config_name = args.config_name
        template_type = args.template_type
        store_aws = args.store_aws if args.store_aws else False
        store_local = args.store_local if args.store_local else False

        with open(json_file, 'r') as file:
            data = json.load(file)

            result = controller_gcg_v2(
                data=data,
                store_aws=store_aws,
                store_local=store_local,
                template_type=template_type,
                name=config_name,
                save_location=save_location
            )

            print("Configuration Generated!")
            if store_local:
                print(f" File Location: {save_location}\{config_name}.txt")

    if args.json is None and args.run is False:
        parser.print_help()


if __name__ == "__main__":
    main()
