#include <stdio.h>

int main(void) {
	int n;
	char name[30];
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%s", name);
		switch (name[0]) {
		case 'A':
			if (name[1] == 'l') printf("204\n");
			else printf("302\n");
			break;
		case 'D':
			printf("207\n");
			break;
		case 'C':
			printf("B101\n");
			break;
		case 'N':
			printf("303\n");
			break;
		case 'S':
			printf("501\n");
			break;
		case 'T':
			printf("105\n");
			break;
		}
	}
	return 0;
}