def is_valid(isbn):
    isbn = isbn.upper()
    print('debug1',isbn)
    isbn = isbn.replace('-','')
    print('debug2',isbn)
    if len(isbn) != 10:
        return False
        # raise ValueError('To check the validity of the isbn ')
    value = 10
    result = 0
    for i in isbn:
        if i == 'X' and value == 1:
            i = 10
        elif ord(i)>=65 and ord(i) <=91:
            return False
        result =result + int(i)*value
        value = value -1
    if result % 11 == 0:
        return True
    else:
        return False
        
        
