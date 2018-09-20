"""
Main file
"""

from datetime import datetime
import get_preferences 
import time
import winsound
import os
import importlib

def show_options():

    """ As the name says - just print available options """

    print('Here are your options: ')
    print('A : Manage preferences. Start here if you are a new user. ')
    print('B : Gather general data e.g. sleep time and mood. ')
    print('C : Start working. ')
    print('D : Add work data manually. ')
    print('q : Quit program and do other things! ')
    print('Please choose one of the options when asked. ')


def get_nice_datetime():

    """ Returns current datetime in my favourite format """

    return datetime.now().strftime('%Y-%m-%d %H:%M')


def yn_input_validator(prompt):

    """ Check if answer is an integer as requested """

    while True:
        answer = input(prompt).lower()
        if answer in ('n', 'no'):
            return False
        elif answer in ('y', 'yes'):
            return True
        else:
            print('I don\'t understand. Can you answer as requested? [y/n] ')


def int_input_validator(prompt):

    """ Checks if input is in correct type """ 

    while True:
        answer = input(prompt)
        try:
            answer = int(answer)
            return answer
        except ValueError:
            print('Please, give me an integer!')


def date_input_validator(prompt):

    """ Check if answer is a date as requested """

    while True:
        answer = input(prompt)
        try:
            answer = datetime.strptime(answer, '%Y-%m-%d').date()
            return answer
        except ValueError:
            print('Please, give me a date! ')


def time_input_validator(prompt):

    """ Check if answer is a time as requested """

    while True:
        answer = input(prompt)
        try:
            time.strptime(answer, '%H:%M')
            return answer
        except ValueError:
            print('Please, give me time! ')


def gather_general_data():
    
    """ Gather additional data """

    is_today = yn_input_validator('Are you adding data from today? [y/n] ')
    directory = 'collected_data'
    file_name = 'general_data.csv'

    while True:
        if is_today:
            day = datetime.now().date()
        else:
            day = date_input_validator('When was this data generated? [YYYY-MM-DD] ')

        actual_get_out_of_bed_time = time_input_validator("What time did you actually get out of bed? [HH:MM] ")
        good_sleep = yn_input_validator("Have you slept well? [y/n] ")
        morning_routine = yn_input_validator("Have you done you morning workout routine? [y/n] ")

        write_to_csv_file(directory, file_name, day, actual_get_out_of_bed_time, good_sleep, morning_routine)
        is_end = yn_input_validator('Is this all of the data you wanted to include? [y/n] ')
        if is_end: break
        is_today = False


def manage_preferences():

    """ View, create or update your preferences """

    is_new_user = yn_input_validator('Are you a new user? [yn] ')

    def show_current_preferences():

        """ Show current preferences """

        print('Your current preferences:')
        print('User name: ' + get_preferences.get_user_name())
        print('Work time unit: ' + str(get_preferences.get_work_time_unit()))
        print('Short break time: ' + str(get_preferences.get_short_break_time()))
        print('Long break time: ' + str(get_preferences.get_long_break_time()))
        print('Work unit bundle: ' + str(get_preferences.get_work_unit_bundle()))


    if is_new_user:
        print('Hello! I\'ll ask you some questions')
        name = input('What is your name? ')
        work_time_unit = int_input_validator("How long would you like your work time unit to last (suggested: 25 min) ? ")
        short_break_time = int_input_validator("How long would you like your break time unit to last (suggested: 5 min) ? ")
        long_break_time = int_input_validator("How long would you like your long break time unit to last (suggested: 15 min) ? ")
        work_unit_bundle = int_input_validator("After what amount of working unit would you like your long break (suggested: 4) ? ")

        try:
            with open('my_preferences.py', 'w') as f:
                f.write('name = \'' + name + '\'\n')
                f.write('work_time_unit = ' + str(work_time_unit) + '\n')
                f.write('short_break_time = ' + str(short_break_time) + '\n')
                f.write('long_break_time = ' + str(long_break_time)+ '\n')
                f.write('work_unit_bundle = ' + str(work_unit_bundle) + '\n')
            importlib.reload(get_preferences)
            show_current_preferences()
        except IOError:
            print('Data file manipulation failed!')
            print(sys.exc_info()[0])
    else:
        show_current_preferences()
        is_change = yn_input_validator('Do you want to change something? [y/n] ')
        if is_change:
            print('Please, pretend you are a new user and just override all data. For now, promise!')

    show_current_preferences()
        

def write_to_csv_file(directory, file_name, *params):

    """ Avoiding repetition """  

    file_address = directory + '/' + file_name
    text = ','.join(str(x) for x in params)

    try:
        with open(file_address, "a+") as f:
            f.write(text + '\n')
    except IOError:
        print('Data file manipulation failed!')
        print(sys.exc_info()[0])


def add_work_data_manually(directory, file_name):

    """ Add data when worked outside of this tool """

    print('So, I understand you worked with somebody else ;(')
    is_today = yn_input_validator('Do you want to insert data only from today? [y/n] ')

    if is_today:
        no_session = int_input_validator('How many pomodoros have you worked today? [int] ')
        day = datetime.now().date()
        write_to_csv_file(directory, file_name, day, no_session)
    else:
        while True: 
            day = date_input_validator('When you worked? [YYYY-MM-DD] ')
            no_session = int_input_validator('How much pomodoros? [int] ')
            write_to_csv_file(directory, file_name, day, no_session)
            is_end = yn_input_validator('Is this the end? [y/n] ')
            if is_end: break


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
    file_name = 'work_data_log.csv'

    while consent:

        no_session = no_session + 1
        print('Starting work unit no ' + str(no_session) + '.')
        work_start_at = get_nice_datetime()
        unit_type = 'work time unit'
        countdown(work_time_unit, 'Work time unit')
        write_to_csv_file(directory, file_name, work_start_at, unit_type)

        if_break = yn_input_validator('Do you want to have a break? [y/n] ')

        if if_break:
            break_start_at = get_nice_datetime()
            break_time = long_break_time if no_session % work_unit_bundle == 0 else short_break_time
            unit_type = 'long break' if break_time > 20 else 'short break'
            print('Starting ' + unit_type)
            countdown(break_time, 'Break')
            write_to_csv_file(directory, file_name, break_start_at, unit_type)

        print('Congratulations for finishing work unit! ')
        consent = yn_input_validator('Do you want to work more? [y/n] ')

    print('That\'s it! Good work, everybody. ')
    return no_session


def main():

    name = 'stranger'
    day = datetime.now().date()
    print('Hello, ' + name + '.')
    show_options()
    action = input('Which one do you choose? ')
    directory = 'collected_data'
    file_name = 'work_data.csv'

    if not os.path.exists(directory):
        try:
            os.makedirs(directory)
        except:
            pass
   
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
            write_to_csv_file(directory, file_name, day, no_session)
        elif action in ('d', 'D'):
            add_work_data_manually(directory, file_name)
        else:
            print('Of course.')
            show_options()
        action = input('If you want to quit, press \'q\'. If not, press something else. ')

    print('Alright, it\'s a wrap!')
    print('Bye, ' + name + '! ')


if __name__ == '__main__':
    main()