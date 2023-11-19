#include <stdio.h>

int main(void) {
	int n;
	long long int result = 1;
	scanf("%d", &n);
	for (int i = n; i >= 1; i--)
		result = result * i;
	printf("%lld", result);
	return 0;
}