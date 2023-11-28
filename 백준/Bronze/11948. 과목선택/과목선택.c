#include <stdio.h>

int main(void) {
	int score[6] = { 0 }, sum = 0;
	for (int i = 0; i < 6; i++)
		scanf("%d", &score[i]);
	for (int i = 0; i < 4; i++) {
		for (int j = i + 1; j < 4; j++) {
			if (score[i] < score[j]) {
				int temp = score[i];
				score[i] = score[j];
				score[j] = temp;
			}
		}
	}
	if (score[5] > score[4]) sum += score[5];
	else sum += score[4];
	sum += score[0] + score[1] + score[2];
	printf("%d", sum);
	return 0;
}