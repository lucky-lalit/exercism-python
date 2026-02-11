def is_armstrong_number(number):
    new_number = str(number)
    total = 0
    count = len(new_number)
    for i in (new_number):
        total = int(i)**count + total
    if total == int(new_number):
        return True
    else:
        return False
    
        
