#include <stdio.h>

int main(void) {
	char score[3];
	scanf("%s", score);
	double result = 0;
	switch (score[0]) {
	case 'A':
		result += 4;
		break;
	case 'B':
		result += 3;
		break;
	case 'C':
		result += 2;
		break;
	case 'D':
		result += 1;
		break;
	}
	switch (score[1]) {
	case '+':
		result += 0.3;
		break;
	case '-':
		result -= 0.3;
		break;
	}
	printf("%.1lf", result);
	return 0;
}