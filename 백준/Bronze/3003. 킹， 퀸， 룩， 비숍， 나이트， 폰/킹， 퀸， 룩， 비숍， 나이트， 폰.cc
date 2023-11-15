#include <stdio.h>

int main(void) {
	int find;
	int result[6] = { 1, 1, 2, 2, 2, 8 };
	for (int i = 0; i < 6; i++) {
		scanf("%d", &find);
		printf("%d ", result[i] - find);
	}
	return 0;
}