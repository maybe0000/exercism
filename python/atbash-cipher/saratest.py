def square(number):
    if number < 1 or number > 64 or number != int(number):
        raise ValueError("Number must be an integer between 1 and 64")
    return 2 ** (number - 1)


def total(number):
    sum = 0
    for i in range(1, number + 1):
        sum += square(i)
    return sum
