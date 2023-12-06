#include <stdio.h>

int main(void) {
	int n, a[1000], b[1000], count = 0;
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
		scanf("%d", &a[i]);
	for (int i = 0; i < n; i++)
		scanf("%d", &b[i]);
	for (int i = 0; i < n; i++)
		if (a[i] <= b[i]) count++;
	printf("%d", count);
	return 0;
}