from data import *


def weapon_check(person):
    # let's see what weapon you've got
    print("Weapon Check Function. person.equip = {}".format(person.equip))
    print("Weapon Check Function. Dictionary response = {}".format(dictionary_weapons[person.equip]))  # fails here at the moment
    return dictionary_weapons[person.equip]

