#include <stdio.h>

int main(void) {
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		for (int j = 0; j <= i; j++)
			printf("*");
		for (int j = 1; j < n * 2 - i * 2 - 1; j++)
			printf(" ");
		for (int j = 0; j <= i; j++)
			printf("*");
		printf("\n");
	}
	for (int i = 1; i < n; i++) {
		for (int j = 0; j < n - i; j++)
			printf("*");
		for (int j = 0; j < i * 2; j++)
			printf(" ");
		for (int j = 0; j < n - i; j++)
			printf("*");
		printf("\n");
	}
	return 0;
}