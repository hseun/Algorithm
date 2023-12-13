#include <string.h>
#include <stdio.h>

int main(void) {
	int t, top, length, j;
	char str[51];
	scanf("%d ", &t);
	for (int i = 0; i < t; i++) {
		top = 0;
		gets(str);
		length = strlen(str);
		for (j = 0; j < length; j++) {
			if (str[j] == '(') top++;
			else  top--;
			if (top < 0) break;
		}
		if (j == length && top == 0) printf("YES\n");
		else printf("NO\n");
	}
	return 0;
}