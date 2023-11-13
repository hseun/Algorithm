#include <stdio.h>
#include <string.h>

int main(void) {
	char str[21];
	int n, r;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d %s", &r, str);
		int length = strlen(str);
		for (int j = 0; j < length; j++) {
			for (int a = 0; a < r; a++)
				printf("%c", str[j]);
		}
		printf("\n");
	}
}