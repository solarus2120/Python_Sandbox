import time
from data import *
# from weapons import *
# from armour import *
# from data import LongBlade


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
