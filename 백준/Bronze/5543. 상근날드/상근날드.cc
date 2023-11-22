#include <stdio.h>

int main(void) {
	int a, b, c, coke, cider, sum = 0;
	scanf("%d %d %d %d %d", &a, &b, &c, &coke, &cider);
	if (coke > cider) sum += cider;
	else sum += coke;
	if (a <= b && a <= c) sum += a;
	else if (b <= a && b <= c) sum += b;
	else sum += c;
	printf("%d", sum - 50);
	return 0;
}