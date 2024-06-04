import datetime

def main():
    print_header()
    birthday = enter_birthday()
    today = datetime.date.today()
    days = birthday_delta(birthday, today)

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
    print(delta.days)
    return delta.days

def print_birthday():


main()

