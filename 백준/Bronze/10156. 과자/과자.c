#include <stdio.h>

int main(void) {
	int k, n, m;
	scanf("%d %d %d", &k, &n, &m);
	int result = (k * n) - m;
	if (result < 0) result = 0;
	printf("%d", result);
	return 0;
}