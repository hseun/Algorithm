#include <stdio.h>

int main(void) {
	int n, minX = 10000, minY = 10000, maxX = -10000, maxY = -10000, x, y;
	scanf("%d", &n);
	if (n == 1) {
		scanf("%d %d", &x, &y);
		printf("0");
		return 0;
	}
	for (int i = 0; i < n; i++) {
		scanf("%d %d", &x, &y);
		if (x > maxX)
			maxX = x;
		if (x < minX)
			minX = x;
		if (y > maxY)
			maxY = y;
		if (y < minY)
			minY = y;
	}
	printf("%d", (maxX - minX) * (maxY - minY));
	return 0;
}