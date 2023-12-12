#include <stdio.h>

int main(void) {
	int n, score = 0, count = 0, temp;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &temp);
		if (temp == 1) {
			count++;
			score += count;
		}
		else count = 0;
	}
	printf("%d", score);
	return 0;
}