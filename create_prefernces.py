"""
Collect user data and preferences to be used later.
Data to be retrieved by get_preference.py
"""


def main():
    new = input("Welcome! Are you a new user? [y/n] ")
    f = open("preferences", "w")
    if new == 'y':
        name = input("What is your name? ")
        work_time = input("How long would you like your work time unit to last? Suggested: 25 min ")
        break_time = input("How long would you like your break time unit to last? Suggested: 5 min ")
        if_long_break = input("Do you want to have long break sometime? [y/n] ")
        if if_long_break == 'y':
            long_break_time = input("How long would you like your long break time unit to last? Suggested: 15 min ")
            long_break_interval = input("After what amount of working unit would you like your long break? Suggested: 4 ")
        elif if_long_break == 'n':
            print("Copy that.")
        else:
            print("Sorry?")
        #todo: write to file
        f.write("name : " + name + '\n')
        f.write("work_time : " + work_time + '\n')
    elif new == 'n':
        print("So, what data would you like to change?")
        print("Your current data: ")
    else:
        print("I don't know what you want.")

    f.close()

if __name__ == "__main__" :
    main()