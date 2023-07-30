from search import search_record


def create(dataset: dict, data: dict):  # Define a function that takes two arguments: 'dataset' (a dictionary)
    # and 'data' (another dictionary).
    dataset.update(data)  # Update the 'dataset' dictionary with the contents of the 'data' dictionary. If they don't
    # exist, new key-value pairs will be added to 'dataset'.
    return dataset


def update(dataset: dict, data: dict):  # Define a function that takes two arguments: 'dataset' (a dictionary)
    # and 'data' (another dictionary).
    dataset.update(data)  # Update the 'dataset' dictionary with the contents of the 'data' dictionary.
    return dataset


def delete(dataset, search_type, value):  # Define a function that takes three arguments: 'dataset' (a dictionary),
    # 'search_type' (a string), and 'value' (a string or number).
    result = search_record(dataset, search_type, value)  # Call the 'search_record()' function with the provided
    # 'dataset', 'search_type', and 'value' to find the records based on the search criteria. Store the search result
    # in the 'result' variable (a dictionary).
    for phone in result.keys():  # Iterate through each phone number (key) in the 'result' dictionary.
        del dataset[phone]  # Delete the phone number (key) and its associated data from the 'dataset' dictionary.
    return dataset
