#include <stdio.h>

int main(void) {
	int key = 0, code;
	for (int i = 0; i < 5; i++) {
		scanf("%d", &code);
		key += code * code;
	}
	key = key % 10;
	printf("%d", key);
	return 0;
}