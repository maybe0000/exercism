def steps(number):
    cnt = 0
    if number < 1 or number != int(number):
        raise ValueError("Only positive integers are allowed")
    while number != 1:
        if number % 2 == 0:
            number /= 2
        else:
            number = number*3 + 1
        cnt += 1
        
    return cnt
