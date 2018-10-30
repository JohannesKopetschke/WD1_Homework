


#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def main():
    secret = random.randint(0, 30)

    while True:
        guess = int(raw_input("Guess the secret number (between 1 and 30): "))  # get user's input and convert it from string into integer (number)

        if guess == secret:
            print "You guessed it - congratulations! It's number" + str(guess)
            break
        elif guess > secret:
            print "You guessed too high. It is not:" + str(guess)
        elif guess < secret:
            print "You guessed too low. It is not:" + str(guess)
        else:
            print "Sorry, your guess is not correct.Secret number is not " + str(guess)

if __name__ == "__main__":  main()