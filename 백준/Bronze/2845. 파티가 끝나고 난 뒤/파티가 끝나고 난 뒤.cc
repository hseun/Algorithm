#include <stdio.h>

int main(void) {
	int l, p, temp;
	scanf("%d %d", &l, &p);
	int person = l * p;
	for (int i = 0; i < 5; i++) {
		scanf("%d", &temp);
		printf("%d ", temp - person);
	}
	return 0;
}