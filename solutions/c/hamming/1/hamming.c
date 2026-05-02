#include "hamming.h"
#include <stdio.h>
#include <string.h>

int compute(const char *lhs, const char *rhs)
{
    int len_lhs = strlen(lhs);
    int len_rhs = strlen(rhs);
    if (len_lhs != len_rhs)
        return -1;
    int count = 0;
    for (int i = 0; i < len_lhs; i++)
    {
        if (lhs[i] != rhs[i])
            count++;
    }
    return count;
    printf("%i",len_lhs);
    printf("%s\n",lhs);
    printf("%s\n",rhs);
    
    // return 0;
}