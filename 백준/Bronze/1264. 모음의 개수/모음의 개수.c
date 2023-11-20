#include <string.h>
#include <stdio.h>

int main(void) {
	char str[256];
	gets(str);
	while (str[0] != '#') {
		int count = 0;
		int length = strlen(str);
		for (int i = 0; i < length; i++)
			if (str[i] == 'A' || str[i] == 'a' || str[i] == 'E' || str[i] == 'e' || str[i] == 'I' || str[i] == 'i' || str[i] == 'O' || str[i] == 'o' || str[i] == 'U' || str[i] == 'u')
				count++;
		printf("%d\n", count);
		gets(str);
	}
	return 0;
}