#include <stdio.h>

int main(void) {
	int n1, n2, a, b, c, d, q, r;
	scanf("%d %d", &n1, &n2);
	a = 100 - n1;
	b = 100 - n2;
	c = 100 - (a + b);
	d = (a * b);
	q = d / 100;
	r = d % 100;
	printf("%d %d %d %d %d %d\n", a, b, c, d, q, r);
	printf("%d %d", q + c, r);
	return 0;
}