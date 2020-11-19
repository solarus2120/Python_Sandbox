class Armour:
    def __init__(self, name, metal, weight, protection):
        self.name = name
        self.metal = metal
        self.weight = weight
        self.protection = protection

    def protect_me(self, protection):
        # do something
        self.protection = protection
        int_protection_event = random.randrange(1, 7, 1)

        if int_protection_event > protection:
            # the armour does nothing
            print("The blow penetrates the armour")
            time.sleep(0.5)
            return False
        else:
            # the armour saves
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
