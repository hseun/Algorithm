#include <stdio.h>

int main(void) {
	int n, result = 1;
	scanf("%d", &n);
	for (int i = 2; i <= n; i++)
		result *= i;
	printf("%d", result);
	return 0;
}