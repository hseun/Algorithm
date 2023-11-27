#include <stdio.h>

int main(void) {
	int oneApple, oneOrange, twoApple, twoOrange;
	scanf("%d %d %d %d", &oneApple, &oneOrange, &twoApple, &twoOrange);
	if (oneApple + twoOrange > twoApple + oneOrange)
		printf("%d", twoApple + oneOrange);
	else
		printf("%d", oneApple + twoOrange);
	return 0;
}