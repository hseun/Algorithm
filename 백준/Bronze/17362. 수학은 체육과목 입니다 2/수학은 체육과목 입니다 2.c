#include <stdio.h>

int main(void) {
	int n, result;
	scanf("%d", &n);
	if (n % 8 <= 5)
		result = (n % 8 != 0) ? n % 8 : 2;
	else if (n % 8 == 6)
		result = 4;
	else result = 3;
	printf("%d", result);
	return 0;
}