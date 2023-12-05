#include <stdio.h>

int main(void) {
	int see = 0, t;
	for (int i = 0; i < 10; i++) {
		scanf("%d", &t);
		if (t == 1) see += 90;
		else if (t == 2) see += 180;
		else if (t == 3) see -= 90;
	}
	see = (see > 0) ? see % 360 : (see * -1) % 360;
	if (see == 0)
		printf("N");
	else if (see == 90)
		printf("E");
	else if (see == 180)
		printf("S");
	else if(see == 270)
		printf("W");
	return 0;
}