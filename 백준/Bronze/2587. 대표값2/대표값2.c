#include <stdio.h>

int main(void) {
    int num[5], sum = 0;
	for (int i = 0; i < 5; i++) {
		scanf("%d", &num[i]);
		sum += num[i];
	}
	int j, key;
	for (int i = 1; i < 5; i++) {
		key = num[i];
		for (j = i - 1; j >= 0 && num[j] > key; j--)
			num[j + 1] = num[j];
		num[j + 1] = key;
	}
	printf("%d\n%d", sum / 5, num[2]);
    return 0;
}