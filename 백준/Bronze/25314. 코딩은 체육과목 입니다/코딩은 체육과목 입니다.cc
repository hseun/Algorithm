#include <stdio.h>

int main(void) {
	int n;
	scanf("%d", &n);
	int count = n / 4;
	for (int i = 0; i < count; i++)
		printf("long ");
	printf("int");
	return 0;
}