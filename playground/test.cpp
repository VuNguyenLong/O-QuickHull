#include <stdio.h>

extern "C"
{
    void hello()
    {
        printf("Hello\n");
    }
}