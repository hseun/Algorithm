#include <stdio.h>

int main(void) {
	int n, k, rank, grade;
	scanf("%d %d", &n, &k);
	for (int i = 0; i < k; i++) {
		scanf("%d", &rank);
		rank = (rank * 100) / n;
		if (rank <= 4) grade = 1;
		else if (rank <= 11) grade = 2;
		else if (rank <= 23) grade = 3;
		else if (rank <= 40) grade = 4;
		else if (rank <= 60) grade = 5;
		else if (rank <= 77) grade = 6;
		else if (rank <= 89) grade = 7;
		else if (rank <= 96) grade = 8;
		else grade = 9;
		printf("%d ", grade);
	}
	return 0;
}