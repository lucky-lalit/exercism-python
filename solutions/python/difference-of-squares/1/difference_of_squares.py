def square_of_sum(number):
    sum = 0
    for i in range(1,number+1):
        # print(i)
        sum = sum + i
    return sum**2
        
def sum_of_squares(number):
    sum_sqr = 0
    for j in range(1,number+1):
        # print(j)
        sum_sqr = sum_sqr + j**2
    return sum_sqr


def difference_of_squares(number):
    return square_of_sum(number)-sum_of_squares(number)
