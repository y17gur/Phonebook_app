import json


def read_dataset(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            dataset = json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    return dataset


def write_dataset(dataset, file_path):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(dataset, file)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
