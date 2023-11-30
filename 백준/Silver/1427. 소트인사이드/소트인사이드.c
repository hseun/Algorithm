#include <stdio.h>
#include <string.h>

int main(void) {
	char num[11], temp;
	scanf("%s", num);
	int length = strlen(num);
	for (int i = 0; i < length; i++) {
		for (int j = i + 1; j < length; j++) {
			if (num[i] < num[j]) {
				temp = num[i];
				num[i] = num[j];
				num[j] = temp;
			}
		}
	}
	printf("%s", num);
}