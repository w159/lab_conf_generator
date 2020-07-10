import argparse

from lcg.app import app
from lcg.env import DEBUG, APP_PORT, APP_HOST


def main():
    parser = argparse.ArgumentParser(description='Lab Configuration Generator')
    parser.add_argument('--run',
                        action='store_true',
                        help="Runs App"
                        )

    args = parser.parse_args()

    if args.run:
        # Enter Execution Code here
        app.run(debug=DEBUG, port=APP_PORT, host=APP_HOST)


if __name__ == "__main__":
    main()
