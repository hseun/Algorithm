#include <stdio.h>

int main(void)
{
    int num, num1, num2, count = 0;
    int num3, result;
    scanf("%d", &num);
    num1 = num / 10;
    num2 = num % 10;
    do
    {
        num3 = ((num1 + num2) % 10);
        result = (num2 * 10) + num3;
        count++;
        num1 = num2;
        num2 = num3;
    } while(result != num);
    printf("%d", count);
}