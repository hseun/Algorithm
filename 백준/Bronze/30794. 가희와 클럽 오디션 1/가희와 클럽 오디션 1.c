#include <stdio.h>

int main(void) {
	int lv, score = 0;
	char judge[8];
	scanf("%d %s", &lv, judge);
	if (judge[0] == 'm') score = 0;
	else if (judge[0] == 'b')
		score = 200 * lv;
	else if (judge[0] == 'c')
		score = 400 * lv;
	else if (judge[0] == 'g')
		score = 600 * lv;
	else if (judge[0] == 'p')
		score = 1000 * lv;
	printf("%d", score);
	return 0;
}