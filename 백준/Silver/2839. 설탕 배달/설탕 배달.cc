#include <stdio.h>

int main(void)
{
    int n, count = 0;
	scanf("%d", &n);
	while (1)
	{
		if (n / 5 > 0)
		{
			if (n % 5 == 0)
			{
				n -= 5;
				count++;
				continue;
			}
			if (n % 5 != 3 && n % 3 == 0)
			{
				n -= 3;
				count++;
				continue;
			}
			n -= 5;
			count++;
			continue;
		}
		if (n / 3 >= 1)
		{
			n -= 3;
			count++;
			continue;
		}
		if (n != 0)
		{
			printf("-1");
			break;
		}
		printf("%d", count);
		break;
	}
    return 0;
}