def square(number):
    if number == 1:
        return 1
    
    elif number > 64 or number < 1:
        raise ValueError("square must be between 1 and 64")
        
    else:
        return 2**(number-1)


def total():
    total_grains = 0
    for item in range(1,65):
        total_grains = total_grains + square(item)
    return total_grains
    
