#include <stdio.h>

int main(void) {
	long long int time = 1;
	int n, week;
	scanf("%d", &n);
	for (int i = 2; i <= n; i++)
		time *= i;
	week = (((time / 60) / 60) / 24) / 7;
	printf("%d", week);
	return 0;
}