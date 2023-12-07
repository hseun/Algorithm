#include <stdio.h>

int main(void) {
	int n, count = 0;
	scanf("%d", &n);
	char str[501] = { '\0' };
	for (int i = 0; i < n; i++) {
		scanf("%s", str);
		int length = strlen(str);
		for (int j = 0; j < length - 1; j++) {
			if ((str[j] == 'O' && str[j + 1] == 'I') || (str[j] == '0' && str[j + 1] == '1')) {
				count++;
				break;
			}
		}
	}
	printf("%d", count);
	return 0;
}