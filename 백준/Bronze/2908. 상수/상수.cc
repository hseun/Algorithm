#include <stdio.h>

int main(void) {
	int num1, num2, num;
	scanf("%d %d", &num1, &num2);
	num1 = ((num1 % 10) * 100) + ((num1 / 10 % 10) * 10) + (num1 / 100);
	num2 = ((num2 % 10) * 100) + ((num2 / 10 % 10) * 10) + (num2 / 100);
	if (num1 > num2)
		num = num1;
	else
		num = num2;
	printf("%d", num);
	return 0;
}