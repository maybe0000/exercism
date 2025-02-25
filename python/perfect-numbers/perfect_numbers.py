def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    
    if number < 1 or number != int(number):
        raise ValueError("Classification is only possible for positive integers.")
    
    def sum_of_factors(number):
        factors = []
        for index in range(1, number//2+1):
            if number % index == 0:
                factors.append(index)
        #print(factors, sum(factors))
        return sum(factors)
    
    aliquot_sum = sum_of_factors(number)
    
    if aliquot_sum == number:
        return "perfect"
    elif aliquot_sum < number:
        return "deficient"
    else:
        return "abundant"
