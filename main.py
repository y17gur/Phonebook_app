from file import read_dataset, write_dataset
from helper import print_result, print_commands, read_values, validate_and_format_phone_number
from manager import create, delete, update
from search import search_record


def main(file_path):
    print_commands()
    dataset = read_dataset(file_path)
    while True:
        command = input('Enter command: ')

        if command == 'new':
            value = validate_and_format_phone_number()
            result = search_record(dataset, command, value)
            if not result:
                print(f'Do you want to create new record for "{value}"?')
                answer = input('y/n? >>> ').lower()
                if answer == 'y':
                    values = read_values(value)  # Call function to collect information for entered phone number
                    dataset = create(dataset, values)  # Call function to add the new phone number and associated data
                    # to the 'dataset'.
                else:
                    print('No records created')
            else:
                print('Record already exists')

        elif command == 'sf':
            value = input('Enter first name: ').lower()
            result = search_record(dataset, command, value)  # Call function to search for records based on the
            # first name and store the result in 'result'.
            print_result(result)  # Call function to print the search result.

        elif command == 'sl':
            value = input('Enter last name: ').lower()
            result = search_record(dataset, command, value)  # Call function to search for records based on the
            # last name and store the result in 'result'.
            print_result(result)  # Call to print the search result.

        elif command == 'sfl':
            value = input('Enter first and last names divided by space: ').lower()
            result = search_record(dataset, command, value)  # Call function to search for records based on the
            # last name and store the result in 'result'.
            print_result(result)

        elif command == 'sp':
            value = validate_and_format_phone_number()
            result = search_record(dataset, command, value)
            print_result(result)

        elif command == 'sct':
            value = input('Enter city: ').lower()
            result = search_record(dataset, command, value)  # Call function to search for records based on the
            # city and store the result in 'result'.
            print_result(result)  # Call function to print the search result.

        elif command == 'sc':
            value = input('Enter country: ').lower()
            result = search_record(dataset, command, value)  # Call function to search for records based on the
            # country and store the result in 'result'.
            print_result(result)  # Call function to print the search result.

        elif command == 'up':
            value = validate_and_format_phone_number()
            result = search_record(dataset, command, value)
            if not result:
                print(f'No records associated with telephone number: {value}\nDo you want to create new record?')
                answer = input('y/n? >>> ').lower()
                if answer == 'y':
                    values = read_values(value)  # Call function to collect information for entered phone number
                    dataset = update(dataset, values)  # Call function to add the new phone number and associated
                    # data to the 'dataset'.
                    print('Record updated successfully.')
                else:
                    print('No records created')
                    pass
            else:
                print_result(result)
                print(f'Do you want to update data for telephone number: "{value}"?')
                answer = input('y/n? >>> ').lower()
                if answer == 'y':
                    values = read_values(value)  # Call function to collect information for entered phone number
                    dataset = create(dataset, values)  # Call function to add the new phone number and associated
                    # data to the 'dataset'.
                    print(f'All ata for telephone number "{value}" was updated.')
                else:
                    print('No records updated')

        elif command == 'del':
            value = validate_and_format_phone_number()
            result = search_record(dataset, command, value)
            if not result:
                print(f'No records associated with telephone number: {value}')
            else:
                print(f'\nDo you want to delete all data for:')
                print_result(result)
                answer = input('y/n? >>> ').lower()
                if answer == 'y':
                    dataset = delete(dataset, command, value)
                    print(f'Data for the telephone number - {value} was deleted')
                else:
                    print('Data was NOT deleted')
                    pass

        elif command == 'help':
            print_commands()

        elif command == 'exit':
            write_dataset(dataset, file_path)
            break

        else:
            print('Not available')


if __name__ == '__main__':
    main('database/database.json')
