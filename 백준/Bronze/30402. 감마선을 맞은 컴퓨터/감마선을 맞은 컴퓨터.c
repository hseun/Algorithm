#include <stdio.h>

int main(void) {
	char pixel;
	int cat = -1;
	for (int i = 0; i < 15; i++) {
		for (int j = 0; j < 15; j++) {
			scanf(" %c", &pixel);
			if (pixel == 'w') {
				cat = 1;
				break;
			}
			else if (pixel == 'b') {
				cat = 2;
				break;
			}
			else if (pixel == 'g') {
				cat = 3;
				break;
			}
		}
		if (cat != -1) break;
	}
	if (cat == 1) printf("chunbae");
	else if (cat == 2) printf("nabi");
	else if (cat == 3)printf("yeongcheol");
	return 0;
}