#include <stdio.h>

int main(void) {
	char subject[51], grade[3];
	double score, scoreSum = 0, gradeScore, result = 0;
	for (int i = 0; i < 20; i++) {
		scanf("%s %lf %s", subject, &score, grade);
		if (grade[0] == 'P') continue;
		scoreSum += score;
		gradeScore = 0;
		switch (grade[0]) {
		case 'A':
			gradeScore += 4;
			break;
		case 'B':
			gradeScore += 3;
			break;
		case 'C':
			gradeScore += 2;
			break;
		case 'D':
			gradeScore += 1;
			break;
		}
		if (grade[1] == '+')
			gradeScore += 0.5;
		result += score * gradeScore;
	}
	printf("%lf", result / scoreSum);
	return 0;
}