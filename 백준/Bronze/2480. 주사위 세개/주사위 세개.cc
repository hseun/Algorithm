#include <stdio.h>

int main(void) {
	int n1, n2, n3, price;
	scanf("%d %d %d", &n1, &n2, &n3);
	if (n1 == n2 && n2 == n3)
		price = 10000 + n1 * 1000;
	else if (n1 == n2 || n1 == n3)
		price = 1000 + n1 * 100;
	else if (n2 == n3)
		price = 1000 + n2 * 100;
	else {
		if (n1 > n2 && n1 > n3)
			price = n1 * 100;
		else if (n2 > n1 && n2 > n3)
			price = n2 * 100;
		else
			price = n3 * 100;
	}
	printf("%d", price);
	return 0;
}