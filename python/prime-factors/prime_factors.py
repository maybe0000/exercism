def factors(value):
    factors = []
    currValue = value
    n = 2
    while n <= currValue:
        if currValue % n == 0:
            factors.append(n)
            currValue /= n
            n = 2
        else:
            n += 1
    return factors
