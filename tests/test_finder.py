import unittest
from finder import find_unique_string


class TestFindUniqueString(unittest.TestCase):
    def test_mango_example(self):
        data = ['apple', 'banana', 'apple', 'mango', 'banana']
        self.assertEqual(find_unique_string(data), 'mango')

    def test_world_example(self):
        data = ['hello', 'world', 'hello']
        self.assertEqual(find_unique_string(data), 'world')

    def test_no_unique(self):
        data = ['hello', 'world', 'hello', 'world']
        self.assertEqual(find_unique_string(data), '')

    def test_empty(self):
        self.assertEqual(find_unique_string([]), '')


if __name__ == '__main__':
    unittest.main()
