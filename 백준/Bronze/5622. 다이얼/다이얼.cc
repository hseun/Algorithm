#include <stdio.h>
#include <string.h>

int main(void) {
	char str[16];
	int time = 0;
	scanf("%s", str);
	int length = strlen(str);
	for (int i = 0; i < length; i++) {
		switch (str[i]) {
		case 'A':
		case 'B':
		case 'C':
			time += 1;
			break;
		case 'D':
		case 'E':
		case 'F':
			time += 2;
			break;
		case 'G':
		case 'H':
		case 'I':
			time += 3;
			break;
		case 'J':
		case 'K':
		case 'L':
			time += 4;
			break;
		case 'M':
		case 'N':
		case 'O':
			time += 5;
			break;
		case 'P':
		case 'Q':
		case 'R':
		case 'S':
			time += 6;
			break;
		case 'T':
		case 'U':
		case 'V':
			time += 7;
			break;
		case 'W':
		case 'X':
		case 'Y':
		case 'Z':
			time += 8;
			break;
		}
		time += 2;
	}
	printf("%d", time);
	return 0;
}