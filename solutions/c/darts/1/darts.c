#include "darts.h"
#include <stdio.h>
#include <math.h>


uint8_t score(coordinate_t landing_position)
{
    float radius = sqrt(pow(landing_position.x,2) + pow(landing_position.y,2));
    if (radius <= 1)
        return 10;
    else if(radius <= 5)
        return 5;
    else if(radius <= 10)
        return 1;
    else
        return 0;
 
}