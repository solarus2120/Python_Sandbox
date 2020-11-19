import sys
from data import *


def who_fights():
    combatant = input("Please enter the combatant name: ") # returns a string, causing issues elsewhere
    print("Who fights Function. combatant = {}".format(combatant))
    # print(dictionary_names[combatant])
    # need to work out how to convert string to object name
    if not dictionary_names[combatant]:
        print("You have entered an invalid name. Exiting")
        exit()
    else:
        return dictionary_names[combatant]
