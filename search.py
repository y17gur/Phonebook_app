def search_record(dataset, search_type, value):  # searches for records in a dataset based on the provided criteria
    result = {}  # Initialize an empty dictionary to store the search results.

    if search_type == 'sp':  # If the search type is 'sp' (search by phone number).
        for phone in dataset:  # Iterate through each phone number in the dataset.
            if value in phone:  # If the entered value is partially or fully present in the phone number.
                result.update({phone: dataset[phone]})  # Add the phone number and its associated data to the result
                # dictionary.

    elif search_type == 'sf':  # If the search type is 'sf' (search by first name).
        for phone, data in dataset.items():
            if value in data['first_name'].lower():
                result.update({phone: dataset[phone]})

    elif search_type == 'sl':  # If the search type is 'sl' (search by last name).
        for phone, data in dataset.items():
            if value in data['last_name'].lower():
                result.update({phone: dataset[phone]})

    elif search_type == 'sfl':  # If the search type is 'sfl' (search by full name).
        values = value.split()  # Split 'value' by spaces and store the parts in 'values'.
        value1 = values[0]  # Assign first part of 'values' to 'value1'.
        if len(values) > 1:
            value2 = values[1]  # Assign second part of 'values' to 'value2'.
        else:
            value2 = ''  # Set value2 to an empty string if there's only one word in 'value'.
        for phone, data in dataset.items():
            if value1 in data['first_name'].lower() and value2 in data['last_name'].lower():
                result.update({phone: dataset[phone]})

    elif search_type == 'sct':  # If the search type is 'sct' (search by city).
        for phone, data in dataset.items().lower():
            if value in data['city']:
                result.update({phone: dataset[phone]})

    elif search_type == 'sc':  # If the search type is 'sc' (search by country).
        for phone, data in dataset.items():
            if value in data['country'].lower():
                result.update({phone: dataset[phone]})

    elif search_type in ['new', 'up', 'del', 'sp']:  # If the search type is 'new', 'up', or 'del'.
        for phone in dataset:
            if value in phone:
                result.update(
                    {phone: dataset[phone]})

    return result
