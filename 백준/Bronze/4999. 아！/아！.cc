#include <string.h>
#include <stdio.h>

int main(void) {
	char str1[1001], str2[1001];
	scanf("%s %s", str1, str2);
	if (strlen(str1) >= strlen(str2))
		printf("go");
	else
		printf("no");
	return 0;
}