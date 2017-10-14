##################################################
## Problem: mastermind.py
## Std: std61
## Name: 
## StudentId: 
##################################################
import random
def compare(number, guess):
    res = [0]*2
    for i in range(len(number)):
        if number[i] == guess[i]:
            res[1]+=1
        elif guess[i] in number:
            res[0]+=1
    return res
number = "{:04d}".format(random.randint(0,9999))
number = input()
guesses = 0
while True:
    guess = input('Guess : ')
    right_wrong = compare(number, guess)
    guesses += 1
    print('X'*right_wrong[1]+'O'*right_wrong[0]+'-'*(4-right_wrong[1]-right_wrong[0]))
    if right_wrong[1] == 4:
        print ('You win the game after {} guess!!!\nThe number was {}'.format(guesses,number))
        break
    elif guesses == 10:
        print('Your guess isn\'t quite right, try again.')
        break
