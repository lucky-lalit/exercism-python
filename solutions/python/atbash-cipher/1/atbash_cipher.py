def encode(plain_text):
    result = ''
    counter = 0
    plain_text = plain_text.lower()
    
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    reverse_aplhabets = "zyxwvutsrqponmlkjihgfedcba"
    
    for letter in plain_text:
        
        if letter.isalnum():
            
            if counter > 0 and counter % 5 == 0:
                result = result + ' '

            if letter.isalpha():
                index = alphabets.index(letter)
                result = result + (reverse_aplhabets[index])
            
            else:
                result = result + letter
            counter = counter + 1
    return result
            


def decode(ciphered_text):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    reverse_aplhabets = "zyxwvutsrqponmlkjihgfedcba"
    ciphered_text = ciphered_text.replace(' ','')
    result=''

    for letter in ciphered_text:
        if letter.isalpha():
            index = reverse_aplhabets.index(letter)
            result = result + alphabets[index]
        else:
            result = result + letter
    return result
        
    
    
