#include <stdio.h>

int main(void) {
    int n, k, score[10000], temp;
	scanf("%d %d", &n, &k);
	for (int i = 0; i < n; i++)
		scanf("%d", &score[i]);
	for (int i = 0; i < n; i++) {
		for (int j = i + 1; j < n; j++) {
			if (score[i] < score[j]) {
				temp = score[i];
				score[i] = score[j];
				score[j] = temp;
			}
		}
	}
	printf("%d", score[k - 1]);
    return 0;
}