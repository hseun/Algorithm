#include <stdio.h>

int main(void) {
	int sum, korean, math, maxKor, maxMath;
	scanf("%d %d %d %d %d", &sum, &korean, &math, &maxKor, &maxMath);
	int korDay = korean / maxKor;
	if (korean % maxKor != 0) korDay++;
	int mathDay = math / maxMath;
	if (math % maxMath != 0) mathDay++;
	if (korDay > mathDay) printf("%d", sum - korDay);
	else printf("%d", sum - mathDay);
	return 0;
}