#include <stdio.h>

int main(void) {
	long long int result, n, m;
	scanf("%lld %lld", &n, &m);
	result = n - m;
	if (result < 0) result *= -1;
	printf("%lld", result);
	return 0;
}