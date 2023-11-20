#include <stdio.h>

int main(void) {
	int n;
	scanf("%d", &n);
	unsigned long long int result = 0;
	for (int i = 1; i <= n; i++)
		result += i;
	printf("%llu\n", result);
	printf("%llu\n", result * result);
	result = 0;
	for (int i = 1; i <= n; i++)
		result += i * i * i;
	printf("%llu\n", result);
	return 0;
}