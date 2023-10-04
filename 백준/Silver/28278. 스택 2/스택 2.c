#include <stdio.h>

int main(void) {
    int n, choice, a;
	int stack[1000000], top = -1;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &choice);
		if (choice == 1) {
			scanf("%d", &a);
			stack[++top] = a;
		}
		else if (choice == 2) {
			if (top == -1)
				printf("-1\n");
			else
				printf("%d\n", stack[top--]);
		}
		else if (choice == 3) {
			printf("%d\n", top + 1);
		}
		else if (choice == 4) {
			if (top == -1)
				printf("1\n");
			else
				printf("0\n");
		}
		else {
			if (top == -1)
				printf("-1\n");
			else
				printf("%d\n", stack[top]);
		}
	}
    return 0;
}