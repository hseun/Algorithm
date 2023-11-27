#include <stdio.h>

int main(void) {
	int day, temp, count = 0;
	scanf("%d", &day);
	for (int i = 0; i < 5; i++) {
		scanf("%d", &temp);
		if (temp == day) count++;
	}
	printf("%d", count);
	return 0;
}