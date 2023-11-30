#include <stdio.h>

int main(void) {
	int a, b, c;
	scanf("%d %d %d", &a, &b, &c);
	int result = (a * (double)b / c > (double)a / b * c) ? a * (double)b / c : (double)a / b * c;
	printf("%d", result);
	return 0;
}