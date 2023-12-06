#include <string.h>
#include <stdio.h>

int main(void) {
	char str[1001];
	gets(str);
	int length = strlen(str);
	int count = 0;
	for (int i = 0; i < length - 3; i++) {
		char temp[6] = { '\0' };
		int t = 0;
		for (int j = i; j < i + 4; j++) {
			temp[t] = str[j];
			t++;
		}
		if (strcmp(temp, "DKSH") == 0) count++;
	}
	printf("%d", count);
	return 0;
}