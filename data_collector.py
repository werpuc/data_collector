"""
Main file
"""

from datetime import datetime
from threading import Thread
import get_preferences 
import time
import winsound
import os


def show_options():

    """ As the name says - just print available options """

    print('Here are your options: ')
    print('A : Manage preferences. Start here if you are a new user. ')
    print('B : Gather general data e.g. sleep time and mood. ')
    print('C : Start working. ')
    print('q : Quit program and do other things! ')
    print('Please choose one of the options when asked. ')


def get_nice_datetime():

    """ Returns date in my fauvorite format """

    return datetime.now().strftime('%Y-%m-%d %H:%M')


def yn_input_validator(prompt):

    """ Check if answer is as requested """

    while True:
        answer = input(prompt).lower()
        if answer in ('n', 'no'):
            answer = False
            break
        elif answer in ('y', 'yes'):
            answer = True
            break
        else:
            print('I don\'t understand. Can you answer as requested? [y/n] ')

    return answer


def gather_general_data():
    pass


def manage_preferences():

    """ View, create or update your preferences """

    is_new_user = yn_input_validator('Are you a new user? ')

    if is_new_user:
        pass
    else:
        print('Your current preferences:')
        print('User name: ' + get_preferences.get_user_name())
        print('Work time unit: ' + str(get_preferences.get_work_time_unit()))
        print('Short break time: ' + str(get_preferences.get_short_break_time()))
        print('Long break time: ' + str(get_preferences.get_long_break_time()))
        print('Work unit bundle: ' + str(get_preferences.get_work_unit_bundle()))


def countdown(countdown_minutes, session_name):

    """ Function to display remaining time. Input wanted in minutes """

    def display(seconds):
        """ Function to format remaing time in user friendly way """
        remaining_minutes, remaining_seconds = divmod(seconds, 60)
        return '{:02d}:{:02d}'.format(remaining_minutes, remaining_seconds)

    countdown_seconds = countdown_minutes # * 60 # for test!

    while countdown_seconds > -1:
        print(display(countdown_seconds), end='\r')
        time.sleep(1)
        countdown_seconds = countdown_seconds - 1

    print(session_name + ' ended.')

    # todo: change melody! this one will get lost
    winsound.PlaySound("SystemExit", winsound.SND_ALIAS)


def working_body(directory, work_time_unit, short_break_time, long_break_time, work_unit_bundle):

    """ Module for tracking time using pomodoro technique """

    no_session = 0
    consent = yn_input_validator('Are you ready to work? [y/n] ')

    f = open(directory+'/work_data_log.csv', 'a+')

    while consent:

        no_session = no_session + 1
        print('Starting work unit no ' + str(no_session) + '.')
        work_start_at = get_nice_datetime()
        unit_type = 'work time unit'
        countdown(work_time_unit, 'Work time unit')
        f.write(str(work_start_at) + ',' + unit_type + '\n')

        if_break = yn_input_validator('Do you want to have a break? [y/n] ')

        if_break:
            break_start_at = get_nice_datetime()
            break_time = long_break_time if no_session % work_unit_bundle == 0 else short_break_time
            unit_type = 'long break' if break_time > 20 else 'short break'
            print('Starting ' + unit_type)
            countdown(break_time, 'Break')
            f.write(str(break_start_at) + ',' + unit_type + '\n')

        print('Congratulations for finishing work unit! ')
        consent = yn_input_validator('Do you want to work more? [y/n] ')

    f.close()
    print('That\'s it! Good work, everybody. ')
    return no_session


def main():

    name = 'stranger'
    day = datetime.now().date()
    print('Hello, ' + name + '.')
    show_options()
    action = input('Which one do you choose? ')
    directory = 'collected_data'

    if not os.path.exists(directory):
        os.makedirs(directory)

    while action != 'q':
        
        if action in ('a', 'A'):
            manage_preferences()
        elif action in ('b', 'B'):
            gather_general_data()
        elif action in ('c', 'C'):
            name = get_preferences.get_user_name()
            work_time_unit = get_preferences.get_work_time_unit()
            short_break_time = get_preferences.get_short_break_time()
            long_break_time = get_preferences.get_long_break_time()
            work_unit_bundle = get_preferences.get_work_unit_bundle()
            no_session = working_body(directory, work_time_unit, short_break_time, long_break_time, work_unit_bundle)

            try:
                f = open(directory+'/work_data.csv', "a+")
                f.write(str(day) + ',' + str(no_session) + '\n')
                f.close()
            except IOError:
                print('Data file manipulation failed!')
                print(sys.exc_info()[0])

        else:
            print('Of course.')
            show_options()
        action = input('If you want to quit, press \'q\'. If not, press something else. ')

    print('Alright, it\'s a wrap!')
    print('Bye, ' + name + '! ')


if __name__ == '__main__':
    main()