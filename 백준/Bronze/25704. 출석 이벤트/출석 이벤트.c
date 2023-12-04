#include <stdio.h>

int main(void) {
	int n, p;
	scanf("%d %d", &n, &p);
	int sale[4] = { p, p, p, p };
	if (n >= 5)
		sale[0] = p - 500;
	if (n >= 10)
		sale[1] = p - (p * (10 / 100.0));
	if (n >= 15)
		sale[2] = p - 2000;
	if (n >= 20)
		sale[3] = p - (p * (25 / 100.0));
	for (int i = 0; i < 4; i++) {
		for (int j = i + 1; j < 4; j++) {
			if (sale[i] > sale[j]) {
				int temp = sale[i];
				sale[i] = sale[j];
				sale[j] = temp;
			}
		}
	}
	printf("%d", (sale[0] > 0) ? sale[0] : 0);
	return 0;
}