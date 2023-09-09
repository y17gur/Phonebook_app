import unittest
from unittest.mock import patch
import json
from file import read_dataset, write_dataset
from helper import print_result, read_values, validate_and_format_phone_number
from manager import create, delete, update


class TestPhonebookApp(unittest.TestCase):

    def setUp(self):
        self.dataset = {
            '+09(876)543-21-36': {
                'first_name': 'wrwear',
                'last_name': 'aert',
                'city': 'New eart',
                'country': 'ert',
            },
            '+54(678)963-74-12': {
                'first_name': 'yyy',
                'last_name': 'ttt',
                'city': 'Los rrr',
                'country': 'eee',
            }
        }
        self.file_path = 'dataset.json'
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(self.dataset, file)

        with open(self.file_path, 'r') as f:
            dataset = json.load(f)

    def test_read_dataset(self):
        result_dataset = read_dataset(self.file_path)
        self.assertEqual(result_dataset, self.dataset)

    def test_write_dataset(self):
        write_dataset(self.dataset, self.file_path)
        with open(self.file_path, 'r', encoding='utf-8') as file:
            result_dataset = json.load(file)
        self.assertEqual(result_dataset, self.dataset)

    @patch('builtins.input',
           side_effect=['+54(678)963-74-12', 'other_first_name', 'other_last_name', 'other_city', 'other_country'])
    def test_read_values_no_phone_number(self, mock_input):
        expected_data = {
            '+54(678)963-74-12': {
                'first_name': 'other_first_name',
                'last_name': 'other_last_name',
                'city': 'other_city',
                'country': 'other_country',
            }
        }
        self.assertEqual(read_values(), expected_data)

    @patch('builtins.print')
    def test_print_result(self, mock_print):
        result_list = {
            '+09(876)543-21-36': {
                'first_name': 'wrwear',
                'last_name': 'aert',
                'city': 'New eart',
                'country': 'ert',
            },
            '+54(678)963-74-12': {
                'first_name': 'yyy',
                'last_name': 'ttt',
                'city': 'Los rrr',
                'country': 'eee',
            }
        }

        print_result(result_list)

        mock_print.assert_any_call('Phone number: +09(876)543-21-36')
        mock_print.assert_any_call('\tFirst_name: wrwear')
        mock_print.assert_any_call('\tLast_name: aert')
        mock_print.assert_any_call('\tCity: New eart')
        mock_print.assert_any_call('\tCountry: ert')
        mock_print.assert_any_call('Phone number: +54(678)963-74-12')
        mock_print.assert_any_call('\tFirst_name: yyy')
        mock_print.assert_any_call('\tLast_name: ttt')
        mock_print.assert_any_call('\tCity: Los rrr')
        mock_print.assert_any_call('\tCountry: eee')

    def test_delete(self):
        search_type = 'sp'
        value = '+54(678)963-74-12'

        expected_dataset = {
            '+09(876)543-21-36': self.dataset['+09(876)543-21-36']
        }

        result_dataset = delete(self.dataset, search_type, value)
        self.assertEqual(result_dataset, expected_dataset)

    def test_create(self):
        data = {
            '+44(123)456-78-90': {
                'first_name': 'new',
                'last_name': 'entry',
                'city': 'New City',
                'country': 'New Country',
            }
        }

        expected_dataset = self.dataset.copy()
        expected_dataset.update(data)

        result_dataset = create(self.dataset, data)
        self.assertEqual(result_dataset, expected_dataset)

    def test_update(self):
        data = {
            '+09(876)543-21-36': {
                'first_name': 'updated',
                'last_name': 'aert',
                'city': 'Updated City',
                'country': 'Updated Country',
            }
        }

        expected_dataset = self.dataset.copy()
        expected_dataset.update(data)

        result_dataset = update(self.dataset, data)
        self.assertEqual(result_dataset, expected_dataset)

    @patch('builtins.input', side_effect=['123456789012'])
    @patch('builtins.print')
    def test_validate_and_format_phone_number_valid(self, mock_print, mock_input):
        expected_output = "+12(345)678-90-12"
        actual_output = validate_and_format_phone_number()
        self.assertEqual(actual_output, expected_output)
        mock_print.assert_called_with("Formatted phone number:", expected_output)

    @patch('builtins.input', side_effect=['123', '123456789012'])
    @patch('builtins.print')
    def test_validate_and_format_phone_number_invalid_then_valid(self, mock_print, mock_input):
        expected_output = "+12(345)678-90-12"
        actual_output = validate_and_format_phone_number()
        self.assertEqual(actual_output, expected_output)
        mock_print.assert_has_calls([
            unittest.mock.call("Invalid input. Please enter exactly 12 digits."),
            unittest.mock.call("Formatted phone number:", expected_output),
        ])


if __name__ == '__main__':
    unittest.main()
