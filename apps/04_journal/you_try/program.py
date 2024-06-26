import journal

# Skeleton
"""
def main():
    print_header()
    run_event_loop()

main()

def print_header():
    pass

def run_event_loop():
    pass

"""
# Want the user to be able to list journal entries, add a journal entry, exit
def print_header():
    print('---------------------------')
    print('       JOURNAL APP')
    print('---------------------------')

def main():
    print_header()
    run_event_loop()

def run_event_loop():

    print('What action would you like to take?')
    cmd = 'EMPTY'
    # list() and [] mean exactly the same thing
    journal_name = 'default'
    journal_data = journal.load(journal_name)


    while cmd != 'x' or cmd:
        cmd = input('[L]ist entries, [A]dd an entry, E[x]ist: ')
        cmd.lower().strip()

        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entry(journal_data)
        elif cmd != 'x' and cmd:
            print("Sorry, {} doesn't tell me what you want".format(cmd))

    print("bye bitch")
    journal.save(journal_name, journal_data)

def list_entries(data):
    print("Your journal entries:")
    entries = reversed(data)
    for idx, entry in enumerate(entries):
        print('*[{}] {}'.format(idx+1, entry))

def add_entry(data):
    text = input('Type or entry, <enter> to exit: ')
    journal.add_entry(text, data)
    # data.append(text)

main()
