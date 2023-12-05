#include <stdio.h>

int main(void) {
	int n, a, b, c, count = 0;
	scanf("%d %d %d %d", &n, &a, &b, &c);
	if (a <= n) count += a;
	else count += n;
	if (b <= n) count += b;
	else count += n;
	if (c <= n) count += c;
	else count += n;
	printf("%d", count);
	return 0;
}