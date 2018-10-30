# -*- coding: utf-8 -*-

menu = {}

while True:
    answer = raw_input("Would you like to insert a dish? (y/n)")
    if answer.lower() != "y":
        break
    dish = raw_input("Please enter the name of your dish")
    price = raw_input ("please enter the price of{}".format(dish))

    menu[dish] = price


for dish in menu:
    text = dish + ": " + menu[dish] + "€\n" #alt +shift + 7
    print (text)
print ("DONE")
