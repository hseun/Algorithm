#include <stdio.h>

int main(void) {
	int black = 0, white = 0;
	char temp;
	for (int i = 0; i < 8; i++) {
		for (int j = 0; j < 8; j++) {
			scanf(" %c", &temp);
			if (temp >= 'a' && temp <= 'z') {
				switch (temp) {
				case 'p': 
					black += 1; 
					break;
				case 'n':
				case 'b':
					black += 3;
					break;
				case 'r':
					black += 5;
					break;
				case 'q':
					black += 9;
					break;
				}
			}
			else {
				switch (temp) {
				case 'P':
					white += 1;
					break;
				case 'N':
				case 'B':
					white += 3;
					break;
				case 'R':
					white += 5;
					break;
				case 'Q':
					white += 9;
					break;
				}
			}
		}
	}
	printf("%d", white - black);
	return 0;
}