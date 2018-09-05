""" File to store and revoke preferences """
from my_preferences import *


def list_current_preferences():
    """ Lists all current preferences """
    pass


def get_user_name():
    """ Returns current user name """
    return name


def get_work_time_unit():
    """ Returns current work time """
    return work_time_unit


def get_short_break_time():
    """ Returns current break time """
    return short_break_time


def get_long_break_time():
    """ Returns current long break time """
    return long_break_time


def get_work_unit_bundle():
    """ Rerturn curren work units bundle - after that amount long break """
    return work_unit_bundle