#include <stdio.h>

int main(void) {
	int t, score[5] = { 0 }, num = 0;
	scanf("%d", &t);
	for (int i = 0; i < t; i++)
		scanf("%d", &score[i]);
	if (score[0] > score[2])
		num += (score[0] - score[2]) * 508;
	else num += (score[2] - score[0]) * 108;
	if (score[1] > score[3])
		num += (score[1] - score[3]) * 212;
	else num += (score[3] - score[1]) * 305;
	num += score[4] * 707;
	num *= 4763;
	printf("%d", num);
	return 0;
}