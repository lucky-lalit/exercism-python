def leap_year(year):
    # if year[-1] == 0 and year[-2] == 0:

    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        
        # if year % 100 == 0 and year % 400 == 0:
            return True
    # elif year % 4 == 0:
        # return True
        
    
    # if (year % 100 == 0 and year % 400 == 0): 
    #     print('debug1')
    #     return True
    # elif year % 4 == 0 and year % 4 != 0:
    #     print('debug2')
    #     return True
    else:
        return False
