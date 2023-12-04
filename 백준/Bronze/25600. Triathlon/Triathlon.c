#include <stdio.h>

int main(void) {
	int n, a, d, g, max = 0, score;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d %d %d", &a, &d, &g);
		score = (a == d + g) ? 2 * (a * (d + g)) : a * (d + g);
		max = (score > max) ? score : max;
	}
	printf("%d", max);
	return 0;
}