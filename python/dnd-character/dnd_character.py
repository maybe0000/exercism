import random


def modifier(value):
    return (value - 10) // 2


class Character:
    def return_random_number(self):
        random_dice = [random.randint(1, 6) for i in range(4)]
        return sum(sorted(random_dice, reverse=True)[:3])

    def __init__(self):
        for attr in [
            "strength",
            "dexterity",
            "constitution",
            "intelligence",
            "wisdom",
            "charisma",
        ]:
            setattr(self, attr, self.return_random_number())

        setattr(self, "hitpoints", 10 + modifier(self.constitution))

    def ability(self):
        return self.constitution
