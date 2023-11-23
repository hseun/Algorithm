#include <stdio.h>

int main(void) {
	int sum[2] = { 0 }, temp;
	for (int i = 0; i < 2; i++) {
		for (int j = 0; j < 4; j++) {
			scanf("%d", &temp);
			sum[i] += temp;
		}
	}
	if (sum[1] > sum[0]) printf("%d", sum[1]);
	else printf("%d", sum[0]);
	return 0;
}