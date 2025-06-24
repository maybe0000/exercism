def prime(number):
    if number < 1:
        raise ValueError("there is no zeroth prime")

    count = 0
    i = 2

    while True:
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                break
        else:
            count += 1
            if count == number:
                return i
        i += 1
