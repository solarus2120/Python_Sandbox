# from data import *
from initiative import *
# from weapons import *
from who_fights import *


def dueller():
    Lucien.introduce()
    Kitania.introduce()
    Cassandra.introduce()

    combatant1 = who_fights()
    combatant2 = who_fights()

#    combatant1 = input("Select the first combatant: ")

    if combatant1 == "Cassandra":
        combatant1 = Cassandra
    elif combatant1 == "Kitania":
        combatant1 = Kitania
    elif combatant1 == "Lucien":
        combatant1 = Lucien
    else:
        print("You have entered an incorrect name. Exiting.")
        exit()

#    combatant2 = input("Select the second combatant: ")

    if combatant2 == "Cassandra":
        combatant2 = Cassandra
    elif combatant2 == "Kitania":
        combatant2 = Kitania
    elif combatant2 == "Lucien":
        combatant2 = Lucien
    else:
        print("You have entered an incorrect name. Exiting")
        exit()

    if combatant1 == combatant2:
        print("{} cannot duel themselves! Exiting".format(combatant1.name))
        exit()

    while combatant1.status != "Dead" and combatant2.status != "Dead":  # and Cassandra.status != "Dead":
        initiative(fight_a=combatant1, fight_b=combatant2)
        time.sleep(1)

    if combatant1.status == "Dead":
        victor = combatant2.name
    else:
        victor = combatant1.name

    print("{} is the winner of the duel! To them go the spoils.".format(victor))
