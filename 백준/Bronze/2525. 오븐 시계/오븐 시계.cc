#include <stdio.h>

int main(void)
{
    int h, m, c;
    int hour, minute;
    scanf("%d %d", &h, &m);
    scanf("%d", &c);
    minute = m + c;
    hour = (minute > 59) ? (h + (minute / 60)) : h;
    minute = (minute > 59) ? (minute % 60) : minute;
    printf("%d %d", hour % 24, minute);
}