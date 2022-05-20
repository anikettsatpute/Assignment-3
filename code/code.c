#include <stdio.h>
#include <math.h>

int main()
{
    double result;

    result = pow(0.3333, 5) + 5 * pow(0.3333, 4) * 2 / 3;
    printf("%f", result);

    return 0;
}