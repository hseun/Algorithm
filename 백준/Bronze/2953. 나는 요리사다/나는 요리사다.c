#include <stdio.h>

int main(void) {
	int score[5] = { 0 }, sum, max = 0, temp;
	for (int i = 0; i < 5; i++) {
		sum = 0;
		for (int j = 0; j < 4; j++) {
			scanf("%d", &temp);
			sum += temp;
		}
		score[i] = sum;
		if (sum > score[max])
			max = i;
	}
	printf("%d %d", max + 1, score[max]);
	return 0;
}