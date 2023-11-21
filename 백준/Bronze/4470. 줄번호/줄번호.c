#include <stdio.h>

int main(void) {
	int n;
	char str[51];
	scanf("%d ", &n);
	for (int i = 1; i <= n; i++) {
		gets(str);
		printf("%d. %s\n", i, str);
	}
	return 0;
}