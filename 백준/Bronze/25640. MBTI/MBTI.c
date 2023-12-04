#include <string.h>
#include <stdio.h>

int main(void) {
	char jinho[5], mbti[5];
	int n, count = 0;
	scanf("%s %d", jinho, &n);
	for (int i = 0; i < n; i++) {
		scanf("%s", mbti);
		if (strcmp(jinho, mbti) == 0)
			count++;
	}
	printf("%d", count);
	return 0;
}