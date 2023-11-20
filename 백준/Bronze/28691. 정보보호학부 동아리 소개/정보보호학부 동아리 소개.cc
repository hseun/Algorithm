#include <stdio.h>

int main(void) {
	char question;
	scanf("%c", &question);
	switch (question) {
	case 'M':
		printf("MatKor");
		break;
	case 'W':
		printf("WiCys");
		break;
	case 'C':
		printf("CyKor");
		break;
	case 'A':
		printf("AlKor");
		break;
	case '$':
		printf("$clear");
		break;
	}
	return 0;
}