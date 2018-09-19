from contextlib import contextmanager
import unittest    
from data_collector import *


@contextmanager
def mockInput(mock):
    original_input = __builtins__.input
    __builtins__.input = lambda _: mock
    yield
    __builtins__.input = original_input


class TestAnswerReturn(unittest.TestCase):
    def testYes(self):
        with mockInput('yes'):
            self.assertEqual(yn_input_validator(''), True)

    def testNo(self):
        with mockInput('no'):
            self.assertEqual(yn_input_validator(''), False)


if __name__ == '__main__':
    unittest.main()