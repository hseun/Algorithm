#include <string.h>
#include <stdio.h>

int main(void) {
	char str[101];
	int mobis[5] = { 0 }, i;
	scanf("%s", str);
	int length = strlen(str);
	for (i = 0; i < length; i++) {
		switch (str[i]) {
		case 'M':
			mobis[0]++;
			break;
		case 'O':
			mobis[1]++;
			break;
		case 'B':
			mobis[2]++;
			break;
		case 'I':
			mobis[3]++;
			break;
		case 'S':
			mobis[4]++;
			break;
		}
	}
	for (i = 0; i < 5; i++)
		if (mobis[i] == 0) break;
	if (i == 5) printf("YES");
	else printf("NO");
	return 0;
}