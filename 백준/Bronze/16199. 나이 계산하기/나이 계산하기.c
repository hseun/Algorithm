#include <stdio.h>

int main(void) {
	int birth[3], standard[3], age[3];
	for (int i = 0; i < 3; i++)
		scanf("%d", &birth[i]);
	for (int i = 0; i < 3; i++)
		scanf("%d", &standard[i]);
	age[1] = standard[0] - birth[0] + 1;
	age[2] = standard[0] - birth[0];
	if (birth[0] <= standard[0] && ((birth[1] == standard[1] && birth[2] <= standard[2]) || birth[1] < standard[1]))
		age[0] = age[2];
	else age[0] = (age[2] > 0) ? age[2] - 1 : age[2];
	for (int i = 0; i < 3; i++)
		printf("%d\n", age[i]);
	return 0;
}