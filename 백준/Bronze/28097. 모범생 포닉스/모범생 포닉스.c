#include <stdio.h>

int main(void) {
	int n, time, sum;
	scanf("%d", &n);
	sum = 8 * (n - 1);
	for (int i = 0; i < n; i++) {
		scanf("%d", &time);
		sum += time;
	}
	int day = sum / 24.0;
	int hour = sum % 24;
	printf("%d %d", day, hour);
	return 0;
}