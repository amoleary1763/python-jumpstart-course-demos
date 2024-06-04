import random

print('-----------------------------')
print('     GUESS THE NUMBER')
print('-----------------------------')


target = random.randint(1, 100)
number = -1

while number != target:
    number = int(input('Guess a number between 1 and 100: '))

    if number > target:
        print("Sorry, {} is too HIGH".format(number))
    elif number < target:
        print("Sucks to suck, {} is too LOW".format(number))
    else:
        print("Wowza! {} is the correct number!".format(number))
print("goodbye.")

'''
Notes: Had a really weird time with indenting (there was an unintentional space) but
otherwise everything went pretty well. Understood while loops and what needs to be 
contained within one. Formatting feature is very nice. 
'''
