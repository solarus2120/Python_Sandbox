import sys
from data import *


def who_fights():
    combatant = input("Please enter the combatant name: ") # returns a string, causing issues elsewhere
    print(combatant)
    # print(dictionary_names[combatant])
    # need to work out how to convert string to object name
    return dictionary_names[combatant]
