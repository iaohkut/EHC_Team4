#include <stdio.h>
#include <math.h>

int main()
{
    int a, b, c;
    float p, s;
    scanf("%d", &a);
    scanf("%d", &b);
    scanf("%d", &c);

    if (a <= b + c && b <= c + a && c <= a + b)
    {
        printf("Day la ba canh cua tam giac");
        p = (a + b + c) / 2;

        s = sqrt(p * (p - a) * (p - b) * (p - c));

        printf("\ndien tich cua tam giac la %f", s);
    }
    else
    {
        printf("day khong phai ba canh cua tam giac");
    }

    return 0;
}