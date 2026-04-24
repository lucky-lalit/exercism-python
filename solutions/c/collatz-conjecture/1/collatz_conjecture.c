#include "collatz_conjecture.h"
#include<stdio.h>

int no_of_steps = 0;
int steps(int start)
{
    if (start < 1)
        return -1;
    
    if (start == 1)
        return 0;
    
    // no_of_steps++;
    
    if (start % 2 == 0)
        return 1 + steps(start/2);
    
    else
        return 1 + steps((start*3)+1);
}