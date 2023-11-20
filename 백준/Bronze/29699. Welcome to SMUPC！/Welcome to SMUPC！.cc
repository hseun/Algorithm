#include <string.h>
#include <stdio.h>

int main(void) {
	int n;
	scanf("%d", &n);
	char str[] = "WelcomeToSMUPC";
	n = (n - 1) % strlen(str);
	if (n < 0) n++;
	printf("%c", str[n]);
	return 0;
}