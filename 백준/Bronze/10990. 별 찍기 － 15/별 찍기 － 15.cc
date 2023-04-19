#include <stdio.h>

int main(void)
{
    int n;
	scanf("%d", &n);
	for (int i = 1; i <= n; i++)
	{
		for (int j = 1; j <= n - i; j++)
		{
			printf(" ");
		}
		if (i > 1) {
			printf("*");
		}
		for (int j = 1; j <= i * 2 - 3; j++)
		{
			printf(" ");
		}
		printf("*\n");
	}
    return 0;
}