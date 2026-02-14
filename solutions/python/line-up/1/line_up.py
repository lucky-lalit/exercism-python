def line_up(name, number):
    number = str(number)
    # print('debug1',number[-1] != 1 and number[-1] !=2 and number[-1] !=3)
    # if number[-1] != 1 and number[-1] !=2 and number[-1] !=3:
    #     return name+', you are the '+number+'th customer we serve today. Thank you!'
    print(number[-1]=='1')
    if len(number) >= 2 and ((number[-1])=='1','2','3','4','5','6','7','8','9','0') and number[-2]=='1':
        return name+', you are the '+number+'th customer we serve today. Thank you!' 
    # elif len(number) > 1 and number[]:
    if number[-1] == '1':
        return name+', you are the '+number+'st customer we serve today. Thank you!'
    elif number[-1] == '2':
        return name+', you are the '+number+'nd customer we serve today. Thank you!'
    elif number[-1] == '3':
        return name+', you are the '+number+'rd customer we serve today. Thank you!'
        
    else:
        return name+', you are the '+number+'th customer we serve today. Thank you!'
    
