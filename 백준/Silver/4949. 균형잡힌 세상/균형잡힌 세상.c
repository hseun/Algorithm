#include <string.h>
#include <stdio.h>

int main(void) {
	char str[101], stack[51];
	int top = -1;
	gets(str);
	while (str[0] != '.') {
		int i, length = strlen(str);
		for (i = 0; i < length; i++) {
			if (str[i] == '(' || str[i] == '[')
				stack[++top] = str[i];
			else if (str[i] == ')' || str[i] == ']') {
				if (top == -1) {
					printf("no\n");
					break;
				}
				else if ((str[i] == ')' && stack[top--] == '[') || (str[i] == ']' && stack[top--] == '(')) {
					printf("no\n");
					break;
				}
			}
			if (i == length - 1) {
				if (top == -1) printf("yes\n");
				else printf("no\n");
			}
		}
		gets(str);
		top = -1;
	}
	return 0;
}