#include <string.h>
#include <stdio.h>

int main(void) {
	char str[101];
	scanf("%s", str);
	int length = strlen(str);
	int arr[26] = { 0 };
	for (int i = 0; i < length; i++)
		arr[str[i] - 97]++;
	for (int i = 0; i < 26; i++)
		printf("%d ", arr[i]);
	return 0;
}