def square(number):
    # when the square value is not in the acceptable range
    if number not in range(1,65):    
        raise ValueError("square must be between 1 and 64")
    return 2**(number-1)


def total():
    sum = 0
    for index in range(1,65):
        sum += square(index)
    return sum