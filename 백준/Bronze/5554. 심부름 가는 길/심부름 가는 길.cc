#include <stdio.h>

int main(void) {
	int second = 0, minute = 0;
	for (int i = 0; i < 4; i++) {
		int temp;
		scanf("%d", &temp);
		second += temp;
	}
	minute = second / 60;
	second = second % 60;
	printf("%d\n%d", minute, second);
	return 0;
}