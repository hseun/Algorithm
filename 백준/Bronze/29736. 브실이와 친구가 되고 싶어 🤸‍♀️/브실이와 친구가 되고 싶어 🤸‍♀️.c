#include <stdio.h>

int main(void) {
	int a, b, k, x, friend = 0;
	scanf("%d %d %d %d", &a, &b, &k, &x);
	for (int i = k - x; i <= k + x; i++) {
		if (i < a || i > b) continue;
		friend++;
	}
	if (friend == 0)
		printf("IMPOSSIBLE");
	else printf("%d", friend);
	return 0;
}