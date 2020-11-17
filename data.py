from people import *
from weapons import *
from armour import *

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