#include <stdio.h>

int main(void) {
	int n, x, price[100000], min = 0;
	scanf("%d %d", &n, &x);
	for (int i = 0; i < n; i++)
		scanf("%d", &price[i]);
	for (int i = 0; i < n - 1; i++) {
		if (price[i] + price[i + 1] < price[min] + price[min + 1])
			min = i;
	}
	printf("%d", (price[min] + price[min + 1]) * x);
	return 0;
}