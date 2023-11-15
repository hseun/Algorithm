#include <stdio.h>

int main(void) {
	int l, time;
	scanf("%d", &l);
	time = (l % 5 == 0) ? l / 5 : l / 5 + 1;
	printf("%d", time);
	return 0;
}