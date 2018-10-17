#!/usr/bin/env python
# -*- coding: utf-8 -*-

#First "hard-code" some number in the program (write the number into a variable). You can call this variable secret.


secret_number = 1

#Then the user has to find out what this number is (using raw_input). Store user's guess in a variable called guess.

guess = int(raw_input("Rate die Zahl (zwischen 1 und 30): "))

#Check if your secret is equal to user's guess.

if guess == secret_number:
    print "Richtig. Herzlichen Glückwunsch"

#If the user's guess is wrong, let him/her know that (use print and if/else).
else:
     print "Schade. Marmelade. Leider falsch!"eee