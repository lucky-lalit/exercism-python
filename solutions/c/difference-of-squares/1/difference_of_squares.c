#include "difference_of_squares.h"
#include <stdio.h>

unsigned int sum_of_squares(unsigned int number)
{
    int sum_of_square = 0;
    for (unsigned int i = 1; i <= number; i++)
    {
        sum_of_square += i*i;
    }
    printf("%i", sum_of_square);
    return sum_of_square;
}
unsigned int square_of_sum(unsigned int number)
{
    int square_of_sum = 0;
    for(unsigned int i = 1; i <= number; i++)
    {
        square_of_sum += i; 
    }
    printf("%i", square_of_sum);
    printf("%i", square_of_sum * square_of_sum);
    return square_of_sum * square_of_sum;
}
unsigned int difference_of_squares(unsigned int number)
{ 
    printf("%i", square_of_sum(number) - sum_of_squares(number));
    return square_of_sum(number) - sum_of_squares(number);
}