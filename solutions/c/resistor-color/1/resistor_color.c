#include "resistor_color.h"
#include <stdio.h>
#include <stdlib.h>

resistor_band_t color[10];
int color_code(resistor_band_t input)
{
    // printf("debug1 %d\n",input);
    // resistor_band_t color = input;
    // printf("debug2 %d\n",color);
    return input;
}

const resistor_band_t *colors()
{
// color = {BLACK,BROWN,RED,ORANGE,YELLOW,GREEN,BLUE,VIOLET,GREY,WHITE};
    // for (int i = 0; i < 9; i++)
    // {
    //     printf("debug 2");
    //     return color[i];
    // }

    color[0] = BLACK;
    color[1] = BROWN;
    color[2] = RED;
    color[3] = ORANGE;
    color[4] = YELLOW;
    color[5] = GREEN;
    color[6] = BLUE;
    color[7] = VIOLET;
    color[8] = GREY;
    color[9] = WHITE;
    
    return color;

}
