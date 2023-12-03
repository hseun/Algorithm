#include <stdio.h>

int main(void) {
	int n, m, result;
	scanf("%d %d", &n, &m);
	if (n > m) result = m / 2;
	else result = n / 2;
	printf("%d", result);
	return 0;
}