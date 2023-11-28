#include <stdio.h>

int main(void) {
	int human[4], x, y, r;
	int index = 0;
	for (int i = 0; i < 4; i++)
		scanf("%d", &human[i]);
	scanf("%d %d %d", &x, &y, &r);
	for (int i = 0; i < 4; i++) {
		if (human[i] == x) {
			index = i + 1;
			break;
		}
	}
	printf("%d", index);
	return 0;
}