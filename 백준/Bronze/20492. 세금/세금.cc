#include <stdio.h>

int main(void) {
	int n;
	scanf("%d", &n);
	int part1 = (int)(n * (78 / 100.0));
	double temp = n * (80 / 100.0);
	int part2 = (int)(temp + ((n - temp) * (78 / 100.0))) ;
	printf("%d %d", part1, part2);
	return 0;
}