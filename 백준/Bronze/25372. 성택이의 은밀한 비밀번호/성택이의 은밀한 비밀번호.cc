#include <stdio.h>
#include <string.h>

int main(void) {
	int n;
	char code[21];
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%s", code);
		if (strlen(code) >= 6 && strlen(code) <= 9)
			printf("yes\n");
		else
			printf("no\n");
	}
	return 0;
}