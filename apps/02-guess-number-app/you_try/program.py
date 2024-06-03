import random

print('--------------------------------')
print('    GUESS THAT NUMBER GAME')
print('--------------------------------')
print()

the_number = random.randint(0,100) # includes both endpoints
guess = -1 # dummy value

name = input('What is your name? ')

# print(guess_text, type(guess_text))
# print(guess, type(guess))

while guess != the_number:
    guess_text = input('Guess a number between 0 and 100: ')
    guess = int(guess_text)

    if guess < the_number:
        print('Sorry {1}, your guess of {0} was too LOW (loser)'.format(guess, name))
    elif guess > the_number:
        print('Sorry idiot, your guess of {} was too HIGH'.format(guess))
    else:
        print('{} wins, whatever, game over'.format(name))
print('done')