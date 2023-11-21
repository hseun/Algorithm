#include <stdio.h>
#include <string.h>

int main(void) {
	int n;
	char name[21];
	scanf("%d ", &n);
	for (int i = 0; i < n; i++) {
		scanf("%s", name);
		int length = strlen(name);
		for (int j = 0; j < length; j++) {
			if (name[j] >= 'A' && name[j] <= 'Z')
				name[j] += 32;
		}
		printf("%s\n", name);
	}
	return 0;
}