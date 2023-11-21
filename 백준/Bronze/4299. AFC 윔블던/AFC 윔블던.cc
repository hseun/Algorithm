#include <stdio.h>

int main(void) {
	int plus, minus, r1, r2;
	scanf("%d %d", &plus, &minus);
	r1 = (plus + minus) / 2;
	r2 = plus - r1;
	if (r1 < 0 || r2 < 0 || r1 + r2 != plus || r1 - r2 != minus) printf("-1");
	else printf("%d %d", r1, r2);
	return 0;
}