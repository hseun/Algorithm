#include <stdio.h>

int main(void) {
	int n, a[1000], b, count = 0;
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
		scanf("%d", &a[i]);
	for (int i = 0; i < n; i++) {
		scanf("%d", &b);
		if (a[i] <= b) count++;
	}
	printf("%d", count);
	return 0;
}