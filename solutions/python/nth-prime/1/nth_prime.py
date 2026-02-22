
def prime(number):
    if number == 0:
        raise ValueError('there is no zeroth prime')
    
    counter = 0
    num = 1
    while counter < number:
        is_prime = True
        num = num + 1
        for i in range(2,int(num**0.5)+1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            counter += 1
    return num
         