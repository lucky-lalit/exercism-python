#include "leap.h"
#include <stdio.h>

// bool leap_year(int year) {
//     printf("debug1 %i", year);
//     return false;
bool leap_year(int year)
{
    printf("%i", year);
    if((year % 4 == 0 && year % 100 != 0) || year % 400 == 0)
    {
        // printf("true");
        return true;
    }
    else 
        return false;
}
