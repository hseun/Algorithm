#include <stdio.h>
#include <string.h>

int main(void) {
	char str[101];
	char c = 'a';
	scanf("%s", str);
	int length = strlen(str);
	for (char c = 'a'; c <= 'z'; c++) {
		for (int i = 0; i < length; i++) {
			if (c == str[i]) {
				printf("%d ", i);
				i = length;
			}
			else if (i == length - 1)
				printf("-1 ");
		}
	}
}