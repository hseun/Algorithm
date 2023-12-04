#include <stdio.h>

int main(void) {
	int a, b, count;
	scanf("%d %d", &a, &b);
	count = (a / 2 > b) ? b : a / 2;
	printf("%d", count);
	return 0;
}