#include <stdio.h>

int main(void) {
	int num1, num2, count = 0, w;
	scanf("%d %d", &num1, &num2);
	int h1 = (num1 % 4 == 0) ? 4 : num1 % 4;
	int h2 = (num2 % 4 == 0) ? 4 : num2 % 4;
	count += (h1 > h2) ? h1 - h2 : h2 - h1;
	int w1 = (num1 % 4 == 0) ? num1 / 4 : num1 / 4 + 1;
	int w2 = (num2 % 4 == 0) ? num2 / 4 : num2 / 4 + 1;
	count += (w1 > w2) ? w1 - w2 : w2 - w1;
	printf("%d", count);
	return 0; 
}