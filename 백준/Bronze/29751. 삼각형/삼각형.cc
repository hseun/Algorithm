#include <stdio.h>

int main(void) {
	int w, h;
	scanf("%d %d", &w, &h);
	double result = (w * h) / 2.0;
	printf("%.1lf", result);
	return 0;
}