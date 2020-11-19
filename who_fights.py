import sys
import data


def who_fights():
    combatant = input("Please enter the combatant name: ") # returns a string, causing issues elsewhere
    print(combatant)
    # need to work out how to convert string to object name
    return combatant
