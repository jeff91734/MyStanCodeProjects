"""
File: hangman.py
Name: Jeff Tsai
-----------------------------
This program plays hangman game.
Users see a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.

N_TURNS = 7


def main():
    """
    The program will ask input guess from user.
    The question is randomly decided, and the answer is dashed.
    User has # of turns making wrong answer.
    If input is greater than 1 letter or non-alphabet, shows error.
    If user make correct guess, display the dashed letter.
    """
    q = random_word()
    ans = q_dis(q)
    turns = N_TURNS
    intro(ans, turns)
    while True:
        guess = input('Your Guess: ')
        if not guess.isalpha():
            print('Illegal format.')
        elif len(guess) != 1:
            print('Illegal format.')
        else:
            guess = guess.upper()
            if guess in q:
                ans = g_find(q, guess, ans)
                correct(ans, turns, guess)
                if ans == q:
                    print('You win!')
                    print('The word was: ' + q)
                    break
            else:
                turns -= 1
                wrong(ans, turns, guess)
                if turns == 0:
                    print('You are completely hung : (')
                    print('The word was: ' + q)
                    break


def intro(ans, turns):
    print('The word look like: ' + ans)
    print('You have ' + str(turns) + ' wrong guesses left.')


def correct(ans, turns, guess):
    print('You are correct !')
    print('The word look like: ' + ans)
    print('You have ' + str(turns) + ' wrong guesses left.')


def wrong(ans, turns, guess):
    print('There is no ' + guess + "\'s in the words")
    print('The word look like: ' + ans)
    print('You have ' + str(turns) + ' wrong guesses left.')


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


def q_dis(q):
    ans = ''
    for i in range(len(q)):
        ans += '-'
    return ans


def g_find(q, guess, ans):
    for i in range(len(q)):
        if q.find(guess, i) != -1:
            j = q.find(guess, i)
            new_ans = ans[:j] + guess + ans[j + 1:len(ans) + 1]
            ans = new_ans
    return ans


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
