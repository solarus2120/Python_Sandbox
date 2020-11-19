from data import *
from weapon_check import *
# from weapons import *
import random
import time


def initiative(fight_a, fight_b):
    int_a_init_check = random.randrange(1, 7, 1)
    int_b_init_check = random.randrange(1, 7, 1)

    wpn_a = None
    wpn_b = None

    wpn_a = weapon_check(fight_a)
    wpn_b = weapon_check(fight_b)

    int_a_init_check = int_a_init_check+wpn_a.init_mod # currently errors here
    int_b_init_check = int_b_init_check+wpn_b.init_mod

    if int_a_init_check > int_b_init_check:  # A has initiative
        if fight_a.energy < wpn_a.energy:
            print("{} is exhausted and cannot strike".format(fight_a.name))
            fight_a.energy += 5
            time.sleep(0.5)
        else:
            fight_a.energy -= wpn_a.energy
            fight_a.strike(fight_b)
    elif int_a_init_check < int_b_init_check:  # B has initiative
        if fight_b.energy < wpn_b.energy:
            print("{} is exhausted and cannot strike".format(fight_b.name))
            fight_b.energy += 5
            time.sleep(0.5)
        else:
            fight_b.energy -= wpn_b.energy
            fight_b.strike(fight_a)
    else:
        print("{} stares at {}, {} stares at {}. Nothing happens".format(fight_a.name, fight_b.name, fight_b.name, fight_a.name))
        time.sleep(0.5)
