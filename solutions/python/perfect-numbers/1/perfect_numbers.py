def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    total = 0
    # divisible = 0
    if number == 0 or number < 0:
        raise ValueError("Classification is only possible for positive integers.")
    for i in range(1,number):
        if number % i == 0:
            total = total + i
    print('debug1',total)
    if total == number:
        return 'perfect'
    elif total > number:
        return 'abundant'
    else:
        return 'deficient'
        
        
