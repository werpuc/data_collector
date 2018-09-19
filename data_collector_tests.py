from contextlib import contextmanager
import unittest    
from data_collector import *


@contextmanager
def mock_input(mock):

	""" prepare input data """
	
    original_input = __builtins__.input
    __builtins__.input = lambda _: mock
    yield
    __builtins__.input = original_input


class test_yn_input_validator(unittest.TestCase):

	""" Tests for yn_input_validator """

    def test_yes(self):
        with mock_input('yes'):
            self.assertEqual(yn_input_validator(''), True)

    def test_no(self):
        with mock_input('no'):
            self.assertEqual(yn_input_validator(''), False)


if __name__ == '__main__':
    unittest.main()