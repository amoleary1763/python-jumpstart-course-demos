import datetime

def main():
    print_header()
    birthday = enter_birthday()
    today = datetime.date.today()
    days = birthday_delta(birthday, today)
    print_birthday(days)

def print_header():
    print("--------------------------------")
    print("         BIRTHDAY APP")
    print("--------------------------------")
def enter_birthday():
    # have to turn these into integers to pass through datetime.date
    year = int(input("What year [YYYY] were you born? "))
    month = int(input("What month [MM] were you born? "))
    day = int(input("What day [DD] were you born? "))

    birthday = datetime.date(year, month, day)
    #print("Your birthday is {}".format(birthday))
    return(birthday)

# Since it's a delta, we're going to have two inputs
def birthday_delta(birthday, today):
    thisyear_birthday = datetime.date(today.year, birthday.month, birthday.day)
    delta = thisyear_birthday - today
    # Only want the days to output
    #print(delta.days)
    return delta.days

def print_birthday(days):
    if days > 0:
        print("Your birthday is {} days away!".format(days))
    elif days < 0:
        print("Your birthday was {} days ago!".format(abs(days)))
    else:
        print("OH MY GOSH HAPPY BIRTHDAY!")

main()

"""
Notes: I'm still kind of confused about this main() function, it's a little different 
way of thinking. He said there's a better way to do this so I'm looking forward to that.
"""