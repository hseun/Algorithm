#include <stdio.h>

int main(void)
{
    int n;
	scanf("%d", &n);
	for (int i = 1; i <= n; i++)
	{
		for (int j = 1; j <= n; j++)
		{		
			printf("* ");
			if (i % 2 != 0 && j == n)
			{
				printf("\n ");
			}
			else if (j == n)
			{
				printf("\n");
			}
		}
	}
    return 0;
}