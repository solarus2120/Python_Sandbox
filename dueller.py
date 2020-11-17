import random
import time


class People:
    def __init__(self, name, status, equip, health, energy, rank, armour_equip):
        self.name = name
        self.status = status
        self.equip = equip
        self.energy = energy
        self.health = health
        self.rank = rank
        self.armour_equip = armour_equip

    def introduce(self):
        print("Hello. My name is " + self.name)
        print("I am a {}, and I am armed with {} and {}".format(self.rank, self.equip, self.armour_equip))

    def strike(self, target):
        print("{} is armed with {} and strikes a mighty blow against {}".format(self.name, self.equip, target.name))
        time.sleep(0.5)

        wpn = None
        amr = None

        if self.equip == LongBlade.name:
            wpn = LongBlade
        elif self.equip == WarAxe.name:
            wpn = WarAxe
        elif self.equip == SmallBlade.name:
            wpn = SmallBlade

        if target.armour_equip == Shirt.name:
            amr = Shirt
        elif target.armour_equip == Hauberk.name:
            amr = Hauberk
        elif target.armour_equip == Byrnie.name:
            amr = Byrnie
        elif target.armour_equip == Suit.name:
            amr = Suit
        elif target.armour_equip == Breastplate.name:
            amr = Breastplate
        elif target.armour_equip == Jack.name:
            amr = Jack

        if not amr.protect_me(amr.protection):
            target.health -= wpn.damage
            if target.health > 9:
                target.status = "Healthy"
            elif target.health > 5:
                target.status = "Lightly Wounded"
            elif target.health > 0:
                target.status = "Heavily Wounded"
            else:
                target.status = "Dead"
            print("{} suffers an injury and is now {}".format(target.name, target.status))
            time.sleep(0.5)


class Weapons:
    def __init__(self, name, energy, damage, init_mod):
        self.name = name
        self.energy = energy
        self.damage = damage
        self.init_mod = init_mod


class Armour:
    def __init__(self, name, metal, weight, protection):
        self.name = name
        self.metal = metal
        self.weight = weight
        self.protection = protection

    def protect_me(self, protection):
        #do something
        self.protection = protection
        int_protection_event = random.randrange(1, 7, 1)

        if int_protection_event > protection:
            #the armour does nothing
            print("The blow penetrates the armour")
            time.sleep(0.5)
            return False
        else:
            #the armour saves
            print("The armour absorbs the blow")
            time.sleep(0.5)
            return True


class Mail(Armour):
    def __init__(self, name, metal, weight, coverage, protection):
        Armour.__init__(self, name, metal, weight, protection)
        self.coverage = coverage


class Leather(Armour):
    def __init__(self, name, metal, weight, animal, protection):
        Armour.__init__(self, name, metal, weight, protection)
        self.animal = animal


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


Lucien = People("Lucien", "Healthy", "Long Blade", 10, 40, "Swordsman", "Suit of Mail")
Kitania = People("Kitania", "Healthy", "War Axe", 10, 40, "Myrmidon", "Leather Breastplate")
Cassandra = People("Cassandra", "Healthy", "Small Blade", 10, 40, "Sneak", "Leather Jack")

LongBlade = Weapons("Long Blade", 10, 2, 0)
WarAxe = Weapons("War Axe", 20, 3, -1)
SmallBlade = Weapons("Small Blade", 5, 1, 1)

Shirt = Mail("Mail Shirt", True, "Light", "Torso", 1)
Hauberk = Mail("Mail Hauberk", True, "Medium", "Torso and Arms", 2)
Byrnie = Mail("Mail Byrnie", True, "Medium", "Head, Torso and Arms", 3)
Suit = Mail("Suit of Mail", True, "Heavy", "Head, Torso, Arms and Legs", 4)
Breastplate = Leather("Leather Breastplate", False, "Light", "Cow", 2)
Jack = Leather("Leather Jack", False, "Light", "Sheep", 1)


def dueller():
    Lucien.introduce()
    Kitania.introduce()
    Cassandra.introduce()

    combatant1 = input("Select the first combatant: ")

    if combatant1 == "Cassandra":
        combatant1 = Cassandra
    elif combatant1 == "Kitania":
        combatant1 = Kitania
    elif combatant1 == "Lucien":
        combatant1 = Lucien
    else:
        print("You have entered an incorrect name")
        exit()

    combatant2 = input("Select the second combatant: ")

    if combatant2 == "Cassandra":
        combatant2 = Cassandra
    elif combatant2 == "Kitania":
        combatant2 = Kitania
    elif combatant2 == "Lucien":
        combatant2 = Lucien
    else:
        print("You have entered an incorrect name")
        exit()

    if combatant1 == combatant2:
        print("{} cannot duel themselves!".format(combatant1.name))
        exit()

    while combatant1.status != "Dead" and combatant2.status != "Dead":  # and Cassandra.status != "Dead":
        initiative(fight_a=combatant1, fight_b=combatant2)
        time.sleep(1)

    if combatant1.status == "Dead":
        victor = combatant2.name
    else:
        victor = combatant1.name

    print("{} is the winner of the duel! To them go the spoils.".format(victor))
