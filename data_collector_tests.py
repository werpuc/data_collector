from contextlib import contextmanager
import unittest    
from data_collector import *


@contextmanager
def mock_input(mock):

    """ Prepare input data """

    original_input = __builtins__.input
    __builtins__.input = lambda _: mock
    yield
    __builtins__.input = original_input


class TestYNInputValidator(unittest.TestCase):

    """ Tests for yn_input_validator """

    def test_yes(self):
        with mock_input('yes'):
            self.assertEqual(yn_input_validator(''), True)

    def test_no(self):
        with mock_input('no'):
            self.assertEqual(yn_input_validator(''), False)

    def test_yes_upper(self):
        with mock_input('YES'):
            self.assertEqual(yn_input_validator(''), True)

    def test_no_upper(self):
        with mock_input('NO'):
            self.assertEqual(yn_input_validator(''), False)


class TestGetNiceDatetime(unittest.TestCase):

	""" Tests for get_nice_datetime """

	def test_current_date_nice_format(self):
		self.assertEqual(get_nice_datetime(), datetime.now().strftime('%Y-%m-%d %H:%M'))

	def test_wrong_date_nice_format(self):
		self.assertNotEqual(get_nice_datetime(), datetime.now())


class TestIntInputValidator(unittest.TestCase):

	""" Tests for int_input_vaidator """

	def test_1(self):
		with mock_input(1):
			self.assertEqual(int_input_validator(''), True)



class TestDateInputValidator(unittest.TestCase):

	""" Tests for date_input_validator """ 

	def test_new_year(self):
		with mock_input('2018-01-01'):
			self.assertEqual(date_input_validator(''), datetime.strptime('2018-01-01', '%Y-%m-%d').date())


class TestTimeInputValidator(unittest.TestCase):

	""" Tests for time_input_validator """

	def test_2137(self):
		with mock_input('21:37'):
			self.assertEqual(time_input_validator(''), '21:37')


class TestGatherGeneralData(unittest.TestCase):

	""" Tests for gather_general_data """ 

	pass


class TestManagePreferences(unittest.TestCase):

	""" Tests for manage_preferences """ 

	pass


class TestWriteToCSVFile(unittest.TestCase):

	""" Tests for write_to_csv_file """ 

	pass


class TestAddWorkDataManually(unittest.TestCase):

	""" Tests for add_work_data_manually """ 

	pass


class TestCountdown(unittest.TestCase):

	""" Tests for countdown """ 

	pass


class TestWorkingBody(unittest.TestCase):

	""" Tests for working_body """ 		
		
	pass


if __name__ == '__main__':
    unittest.main()