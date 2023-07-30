# A 'base_dict' dictionary serves as a template for storing information related to a phone number.
base_dict = {
    'phone_number': {
        'first_name': '',
        'last_name': '',
        'city': '',
        'country': '',
    }
}
# These lists are used later to iterate through the data fields when collecting information.
keys = ['first_name', 'last_name', 'city', 'country']
values = ['first_name', 'last_name', 'city', 'country']


# The function that displays a list of available commands for the user.
def print_commands():
    print('Available  commands:',
          'new - Add new entries',
          'sf - Search by first name',
          'sl - Search by last name',
          'sfl - Search by full name',
          'sp - Search by telephone number',
          'sct - Search by city',
          'sc - Search by country',
          'up - Update a record for a given telephone number',
          'del - Delete a record for a given telephone number',
          'help - list of available commands',
          'exit - An option to exit the program', sep='\n')


# A function that takes a dictionary 'result_list' as input.
def print_result(result_list):
    for phone, data in result_list.items():  # Iterate through each key-value pair in 'result_list', where 'phone' is
        # the key, and 'data' is the value (another dictionary).
        print(f'Phone number: {phone}')  # Print the phone number associated with the current record.
        for name, record in zip(values, data):  # Iterate through the 'data' dictionary using 'zip' with 'values',
            # where 'name' represents the data field name, and 'record' represents the corresponding value.
            print(f'\t{name.capitalize()}: {data[record]}')  # Print the capitalized 'name' (data field name) and its
            # associated 'record' (value) from the 'data' dictionary.


def read_values(phone_number=None):
    if phone_number:
        phone = phone_number
    else:
        phone = input('Enter phone number: ')
    new_data = {phone: {}}
    for key, value in zip(keys, values):
        new_data[phone][key] = input(f'Enter {value}: ')
    return new_data


def validate_and_format_phone_number():
    while True:
        phone_number = input("Enter your 12-digit phone number: ")
        digits = ''.join(filter(str.isdigit, phone_number))  # Remove any non-digit characters from the input
        if len(digits) == 12:
            formatted_number = f"+{digits[0:2]}({digits[2:5]}){digits[5:8]}-{digits[8:10]}-{digits[10:12]}"
            print("Formatted phone number:", formatted_number)
            return formatted_number
        else:
            print("Invalid input. Please enter exactly 12 digits.")
