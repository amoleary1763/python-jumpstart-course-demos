"""
This is the journal module
"""


import os
def load(name):
    """
    This method loads and loads a new journal.

    :param name: This base name of the journal to load.
    :return: A new journal data structure populated with the file data.
    """
    data = []
    filename = get_full_pathname(name)
    if os.path.exists(filename):
        with open(filename) as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())
    return data # storing the data as the list


"""def save(name, journal_data):
    # base_dir = "~/myworkingfolder"
    # rel_dir = 'data/temp.txt'
    # full_file = base_dir + '/' + rel_dir

    filename = os.path.join('./journal/', name + '.jrl')
    print("... saving to: {}".format(filename))


    #fout = open(filename, 'w') # w for write, r for read
    with open(filename, 'w' as fout:)
        for entry in journal_data:
           fout.write(entry + '\n')

    # fout.close() : don't need this because of with statement """

# cleaned up function
def save(name, journal_data):
    filename = get_full_pathname(name)
    print("... saving to: {}".format(filename))

    with open(filename, 'w') as fout:
        for entry in journal_data:
           fout.write(entry + '\n')

def get_full_pathname(name):
    #C:\Users\ameli\PycharmProjects\python-jumpstart-course-demos\apps\04_journal\final\journals
    # on windows this is an issue ^^ is showing up with double \\
    filename = os.path.abspath(os.path.join('journals', name + '.jrl'))
    return(filename)

def add_entry(text, journal_data):
    journal_data.append(text)

