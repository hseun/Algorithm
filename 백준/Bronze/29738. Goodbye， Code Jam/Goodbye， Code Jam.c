#include <stdio.h>

int main(void) {
	int t, n, round;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		scanf("%d", &n);
		if (n <= 25) round = 4;
		else if (n <= 1000) round = 3;
		else if (n <= 4500) round = 2;
		else round = 1;
		if (round == 4)
			printf("Case #%d: World Finals\n", i);
		else
			printf("Case #%d: Round %d\n", i, round);
	}
	return 0;
}