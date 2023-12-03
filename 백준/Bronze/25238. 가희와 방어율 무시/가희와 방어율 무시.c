#include <stdio.h>

int main(void) {
	int a, b, d;
	scanf("%d %d", &a, &b);
	d = a - (a * (b / 100.0));
	if (d < 100) printf("1");
	else printf("0");
}