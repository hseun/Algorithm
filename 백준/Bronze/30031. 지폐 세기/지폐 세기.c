#include <stdio.h>

int main(void) {
	int n, h, w, sum = 0;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d %d", &w, &h);
		if (w == 136) sum += 1000;
		else if (w == 142) sum += 5000;
		else if (w == 148) sum += 10000;
		else if (w == 154) sum += 50000;
	}
	printf("%d", sum);
	return 0;
}