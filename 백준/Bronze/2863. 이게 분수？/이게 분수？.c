#include <stdio.h>

int main(void) {
	int a, b, c, d, max = 0, temp, count = 0;
	scanf("%d %d %d %d", &a, &b, &c, &d);
	for (int i = 0; i < 4; i++) {
		temp = (int)((double)a / c + (double)b / d);
		if (temp >= max) {
			max = temp;
			count = i;
		}
		temp = a;
		a = c;
		c = d;
		d = b;
		b = temp;
	}
	printf("%d", count);
	return 0;
}