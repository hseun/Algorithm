#include <stdio.h>

int main(void) {
	char unit[4];
	int t;
	double temp;
	scanf("%d", &t);
	for (int i = 0; i < t; i++) {
		scanf("%lf %s", &temp, unit);
		if (unit[0] == 'k')
			printf("%.4lf lb\n", temp * 2.2046);
		else if (unit[0] == 'g')
			printf("%.4lf l\n", temp * 3.7854);
		else {
			if (unit[1] == 'b')
				printf("%.4lf kg\n", temp * 0.4536);
			else printf("%.4lf g\n", temp * 0.2642);
		}
	}
	return 0;
}