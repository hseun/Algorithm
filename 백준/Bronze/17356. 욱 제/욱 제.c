#include <stdio.h>
#include <math.h>

int main(void) {
	int a, b;
	scanf("%d %d", &a, &b);
	double m = (b - a) / 400.0;
	double wookWin = 1 / (1 + pow(10, m));
	printf("%lf", wookWin);
	return 0;
}