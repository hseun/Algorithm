#include <stdio.h>

int main(void) {
	int m, x, y, cup[4] = { 0, 1, 0, 0 };
	scanf("%d", &m);
	for (int i = 0; i < m; i++) {
		scanf("%d %d", &x, &y);
		int temp = cup[x];
		cup[x] = cup[y];
		cup[y] = temp;
	}
	for(int i = 1; i < 4; i++)
		if (cup[i] != 0) {
			printf("%d", i);
			break;
		}
	return 0;
}