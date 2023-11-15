#include <stdio.h>

int main(void) {
	int arrA[100][100], arrB[100][100];
	int n, m;
	scanf("%d %d", &n, &m);
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
			scanf("%d", &arrA[i][j]);
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
			scanf("%d", &arrB[i][j]);
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++)
			printf("%d ", arrA[i][j] + arrB[i][j]);
		printf("\n");
	}
	return 0;
}