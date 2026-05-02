#include "resistor_color_duo.h"
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

uint16_t color_code(const resistor_band_t *pair)
{

    char str1[3];
    char str2[2];
    sprintf(str1,"%d",pair[0]);
    sprintf(str2,"%d",pair[1]);
    strcat(str1,str2);
    printf("%s",str1);
    
    printf("%i",pair[0]);
    printf("%i\n",pair[1]);
    printf("%i\n",pair[0]+pair[1]);
    return atoi(str1);
}