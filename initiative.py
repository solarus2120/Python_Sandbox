from data import *
from weapons import *
import random, time


def initiative(fight_a, fight_b):
    int_a_init_check = random.randrange(1, 7, 1)
    int_b_init_check = random.randrange(1, 7, 1)

    wpn_a = None
    wpn_b = None

    if fight_a.equip == LongBlade.name:
        wpn_a = LongBlade
    elif fight_a.equip == WarAxe.name:
        wpn_a = WarAxe
    elif fight_a.equip == SmallBlade.name:
        wpn_a = SmallBlade

    if fight_b.equip == LongBlade.name:
        wpn_b = LongBlade
    elif fight_b.equip == WarAxe.name:
        wpn_b = WarAxe
    elif fight_b.equip == SmallBlade.name:
        wpn_b = SmallBlade

    int_a_init_check = int_a_init_check+wpn_a.init_mod
    int_b_init_check = int_b_init_check+wpn_b.init_mod

    if int_a_init_check > int_b_init_check:  #A has initiative
        if fight_a.energy < wpn_a.energy:
            print("{} is exhausted and cannot strike".format(fight_a.name))
            fight_a.energy += 5
            time.sleep(0.5)
        else:
            fight_a.energy -= wpn_a.energy
            fight_a.strike(fight_b)
    elif int_a_init_check < int_b_init_check:  #B has initiative
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