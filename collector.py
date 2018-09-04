"""
Welcome to DataCollector!
The place to be if you want to track your working routine and (questionably) be proud of yourself.
"""

from datetime import datetime
import get_preferences

print(__doc__)


def gather_general_data(day):
    """ Get general data e.g. sleep, mood as reference and write it down in dedicated file """
    print("Let's gather some data!")
    actual_day_start = input("When did you actually get out of bed? ")
    if_slept_well = input("Have you slept well? ")
    if_morning_routine = input("Have you done you morning workout routine? ")
    f = open("my_daily_data.csv", "a+")
    f.write( str(day) + ',' + actual_day_start + ',' + str(input_validator(if_slept_well)) + ',' + str(input_validator(if_morning_routine)) + '\n')
    f.close()
    # print(str(day), actual_day_start, input_validator(if_slept_well), input_validator(if_morning_routine))


def input_validator(answer):
    """Check if answer is as requested"""
    if answer == 'n':
        answer = False
    elif answer == 'y':
        answer = True
    else:
        print("I don't understand. Let's call it 'no' ")
        return 0
    return int(answer)


def working_body(work_time, short_break_time, long_break_time):
    no_session = 0
    # todo: while
    no_session = no_session + 1
    print("Start working session no. " + str(no_session))
    # todo: countdown
    if no_session % 4 == 0:
        print("Time for long break")
        break_time = long_break_time
    else:
        print("Time for short break")
        break_time = short_break_time

    # todo: the same for break
    return no_session

    # todo : summary after everything


def main():
    day = datetime.now().date()

    name = get_preferences.get_user_name()
    work_time_unit = get_preferences.get_work_time_unit()
    short_break_time = get_preferences.get_short_break_time()
    long_break_time = get_preferences.get_long_break_time()

    print("Hello " + name + ". Welcome at this beautiful day of " + str(day))
    gather_general_data(day)

    consent = input("Are you ready to start working today? [y/n] ")
    input_validator(consent)
    if consent:
        no_session = working_body(work_time_unit, short_break_time, long_break_time)
        print("Today you worked " + str(no_session) + " units of time. Congrats!")
    print("Bye, " + name)



if __name__ == "__main__":
    main()