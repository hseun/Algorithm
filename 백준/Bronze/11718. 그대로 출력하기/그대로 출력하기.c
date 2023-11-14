#include <stdio.h>

int main(void) {
	char str[101];
	while (gets(str) != NULL)
		printf("%s\n", str);
	return 0;
}