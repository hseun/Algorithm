#include <stdio.h>

int main(void) {
	int n, a, b;
	scanf("%d %d %d", &n, &a, &b);
	if (a == b)
		printf("Anything\n");
	else if (a <= b)
		printf("Bus\n");
	else
		printf("Subway\n");
	return 0;
}