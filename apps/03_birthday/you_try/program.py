import datetime

#### Below is the sketch/skeleton of the program we want to create:
"""
def print_header():
    pass

def get_birthday_from_user():
    pass

def compute_days_between_dates():

def print_birthday_information():
    pass

def main():
    print_header()
    bday = get_birthday_from_user()
    now = None
    numbere_of_days = compute_days_between_dates(bday, now)
    print_birthday_information()

"""
def print_header():
    print('----------------------------')
    print('       BIRTHDAY APP')
    print('----------------------------')
    print()

def get_birthday_from_user():
    print('When were you born?')
    year = int(input('Year [YYYY]: '))
    month = int(input('Month [MM]: '))
    day = int(input('Day [DD]: '))

    birthday = datetime.date(year, month, day)
    return birthday

def compute_days_between_dates(original_date, target_date):
    this_year = datetime.date(target_date.year, original_date.month, original_date.day)

    dt = this_year-target_date
    return dt.days

def print_birthday_information(days):
    if days < 0:
        print("You had your birthday {} days ago!".format(abs(days)))
    elif days > 0:
        print("Your birthday is in {} days".format(days))
    else:
        print("HAPPY BIRTHDAY OH MY GOSH CONGRATULATIONS")

def main():
    print_header()
    bday = get_birthday_from_user()
    today = datetime.date.today()
    number_of_days = compute_days_between_dates(bday, today)
    print_birthday_information(number_of_days)

main()