#include <stdio.h>

int main(void) {
	int startHour, startMinute, startSecond;
	int endHour, endMinute, endSecond;
	int hour, second, minute;
	for (int i = 0; i < 3; i++) {
		scanf("%d %d %d %d %d %d", &startHour, &startMinute, &startSecond, &endHour, &endMinute, &endSecond);
		second = (endSecond - startSecond >= 0) ? endSecond - startSecond : endSecond - startSecond + 60;
		minute = (endMinute - startMinute >= 0) ? endMinute - startMinute : endMinute - startMinute + 60;
		minute = (endSecond - startSecond >= 0) ? minute : minute - 1;
		hour = (minute >= 0) ? (endHour - startHour) : (endHour - startHour - 1);
		hour = (endMinute - startMinute >= 0) ? hour : hour - 1;
		minute = (minute >= 0) ? minute : minute + 60;
		printf("%d %d %d\n", hour, minute, second);
	}
	return 0;
}