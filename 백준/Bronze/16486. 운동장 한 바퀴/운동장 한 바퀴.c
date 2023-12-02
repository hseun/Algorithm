#include <stdio.h>

int main(void) {
	int d1, d2;
	double pie = 3.141592;
	scanf("%d %d", &d1, &d2);
	double result = (2 * d1) + (2 * pie * d2);
	printf("%lf", result);
	return 0;
}