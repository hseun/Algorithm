#include <stdio.h>
#include <string.h>

int main(void) {
	char str[1001];
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%s", str);
		printf("%c%c\n", str[0], str[strlen(str) - 1]);
	}
	return 0;
}