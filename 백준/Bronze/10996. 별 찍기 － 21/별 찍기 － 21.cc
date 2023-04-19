#include <stdio.h>

int main(void)
{
    int n;
	scanf("%d", &n);
	for (int i = 1; i <= n; i++)
	{
		if (n % 2 == 0) {
			for (int j = 1; j <= 2; j++)
			{
				for (int a = 1; a <= n / 2; a++)
				{
					printf("* ");
				}
				if (j % 2 == 0) {
					printf("\n");
				}
				else {
					printf("\n ");
				}
			}
		}
		else {
			for (int a = 1; a <= (n + 1) / 2; a++)
			{
				printf("* ");
			}
			printf("\n ");
			for (int b = 1; b <= n / 2; b++) 
			{
				printf("* ");
			}
			printf("\n");
		}
	}
    return 0;
}