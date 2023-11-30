#include <stdio.h>

int main(void) {
	int a, b, c, d, e, time = 0;
	scanf("%d %d %d %d %d", &a, &b, &c, &d, &e);
	if (a < 0) {
		time += d;
		for (; a != 0; a++)
			time += c;
	}
	for (; a != b; a++)
		time += e;
	printf("%d", time);
	return 0;
}