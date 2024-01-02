#include <stdio.h>

int main(void) {
	int n, sum, min, num;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		sum = 0;
		min = 100;
		for (int j = 0; j < 7; j++) {
			scanf("%d", &num);
			if (num % 2 == 0) {
				sum += num;
				if (num < min)
					min = num;
			}
		}
		printf("%d %d\n", sum, min);
	}
	return 0;
}