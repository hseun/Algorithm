#include <stdio.h>

int main(void) {
	int v, a, b, day = 0;
	scanf("%d %d %d", &a, &b, &v);
	v = v - b;
	day += v / (a - b);
	if (v % (a - b) > 0) day++;
	printf("%d", day);
	return 0;
}