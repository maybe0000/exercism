import random
import string


def get_random_robot_name(used_names):
    def gen_name():
        letters = random.choices(string.ascii_uppercase, k=2)
        digits = random.choices(string.digits, k=3)
        return "".join(letters + digits)

    while (name := gen_name()) in used_names:
        pass
    return name


class Robot:
    used_names = set()

    def __init__(self):
        name = get_random_robot_name(Robot.used_names)
        Robot.used_names.add(name)
        self.name = name

    def reset(self):
        old_name = self.name
        name = get_random_robot_name(Robot.used_names)
        Robot.used_names.add(name)
        self.name = name
        Robot.used_names.remove(old_name)
