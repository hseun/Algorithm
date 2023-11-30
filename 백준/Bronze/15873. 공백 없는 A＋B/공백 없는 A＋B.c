#include <stdio.h>
#include <string.h>

int main(void) {
	char temp[5];
	int a, b;
	scanf("%s", temp);
	int length = strlen(temp);
	if (length == 2) {
		a = temp[0] - '0';
		b = temp[1] - '0';
	}
	else if (length == 4) {
		a = 10;
		b = 10;
	}
	else {
		if (temp[1] == '0') {
			a = 10;
			b = temp[2] - '0';
		}
		else {
			a = temp[0] - '0';
			b = 10;
		}
	}
	printf("%d", a + b);
	return 0;
}