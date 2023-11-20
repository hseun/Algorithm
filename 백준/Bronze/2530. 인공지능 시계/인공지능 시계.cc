#include <stdio.h>

int main(void) {
	int h, m, s, during;
	scanf("%d %d %d %d", &h, &m, &s, &during);
	s += during;
	m += s / 60;
	s = (s >= 60) ? s % 60 : s;
	h += m / 60;
	m = (m >= 60) ? m % 60 : m;
	h = (h >= 24) ? h % 24 : h;
	printf("%d %d %d", h, m, s);
	return 0;
}