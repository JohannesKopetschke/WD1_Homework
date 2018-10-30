
#Program greets user and describes what's the purpose of the program

print "Hello to the KM into Miles converter"
#Program asks user to enter number of kilometers.


while True:
    print "Bitte Kilometeranzahl eingeben"
    km = raw_input("Kilometers: ")

    try:
        miles = km * 0.6

        print "{0} kilometers is {1} miles.".format(km, miles)
    except Exception as e:
        print "Please enter a number, not text!"

    choice = raw_input("Would you like to do another conversion (y/n): ")

    if choice.lower() != "y" and choice.lower() != "yes":
        break


#User enters the amount of kilometers.
#Program converts these kilometers into miles and prints them.
#Program asks user if they'd want to do another conversion.
#If yes, repeat the above process (except the greeting).
#If not, program says goodbye and stops.