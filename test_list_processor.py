import unittest
from list_processor import process_list

class TestProcessList(unittest.TestCase):
    def test_process_list_valid_length(self):
        input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        processed_list = process_list(input_list)
        self.assertEqual(len(processed_list), 14)

    def test_process_list_invalid_length(self):
        input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        with self.assertRaises(ValueError):
            process_list(input_list)

if __name__ == '__main__':
    unittest.main()
