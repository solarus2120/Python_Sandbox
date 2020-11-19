from data import *


def weapon_check(person):
    # let's see what weapon you've got
    print(person.equip) # is a string at the moment, causing issues elsewhere
    return dictionary_weapons[person.equip]
