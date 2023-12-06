#include <stdio.h>

int main(void) {
	int a, b, max = 3;
	scanf("%d %d", &a, &b);
	a -= 2;
	b -= 1;
	if (a > b) max += (2 * b);
	else max += (2 * a);
	printf("%d", max);
	return 0;
}