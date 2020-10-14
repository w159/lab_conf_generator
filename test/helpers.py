import json

TEST_DATA_DIR = 'data'


def open_json_file(file_name):
    with open(f'{TEST_DATA_DIR}/{file_name}') as file:
        data = json.load(file)

    return data
