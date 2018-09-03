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
    print(str(day), input_validator(if_slept_well))


def input_validator(answer):
    """Check if answer is as requested"""
    if answer == 'n':
        answer = False
    elif answer == 'y':
        answer = True
    else:
        print("Please, be kind to me and answer as requested")
    return int(answer)


def working_body(consent, work_time, short_break_time, long_break_time):
    no_session = 0
    if consent:
        no_session = no_session + 1
        print("Start working session no. " + str(no_session))
        # todo: countdown
        if no_session % 4 == 0:
            print("Time for long break")
            break_time = long_break_time
        else:
            print("Time for short break")
        # todo: the same for break
    return no_session

    # todo: while
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
    no_session = working_body(consent, work_time_unit, short_break_time, long_break_time)
    print("Bye, " + name)
    print("Today you worked "+str(no_session)+" units of time. Congrats!")


if __name__ == "__main__":
    main()