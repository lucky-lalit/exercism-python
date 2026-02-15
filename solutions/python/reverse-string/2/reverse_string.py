def reverse(text):
    revers_str = ''
    for i in range(1,len(text)+1):
        print(text[-i])
        revers_str = revers_str + (text[-i])
        print('debug1',revers_str)
    return revers_str
        
        
