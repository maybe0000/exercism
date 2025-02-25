"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


EXPECTED_BAKE_TIME = 40

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME-elapsed_bake_time


# You might also consider defining a 'PREPARATION_TIME' constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations.

def preparation_time_in_minutes(number_of_layers):
    """Calculate preparation time in minutes

    :param number_of_layers: int - number of layers in the lasagna
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the number of layers the lasagna has and returns how many minutes
    you would spend making them, if each layer takes 2 minutes to prepare.
    """
    return number_of_layers*2


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate total elapsed cooking time (prep + bake) in minutes

    :param number_of_layers: int - number of layers in the lasagna
    :param elapsed_bake_time: int - number of minutes the lasagna has been baking in the oven
    :return: int - total number of minutes you have been cooking

    Function that takes the number of layers the lasagna has and the number of minutes the lasagna
    has already been baking in the oven and returns the sum of the total preparation time and 
    how much time lasagna has already spent baking.
    """
    return preparation_time_in_minutes(number_of_layers)+elapsed_bake_time