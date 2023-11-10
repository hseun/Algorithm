#include <stdio.h>

int main(void) {
	int stack[1000000];
	int n, top = -1, command, item;
	scanf("%d ", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d ", &command);
		switch (command) {
		case 1:
			scanf("%d ", &item);
			stack[++top] = item;
			break;
		case 2:
			if (top == -1) printf("-1\n");
			else printf("%d\n", stack[top--]);
			break;
		case 3:
			printf("%d\n", top + 1);
			break;
		case 4:
			if (top == -1) printf("1\n");
			else printf("0\n");
			break;
		case 5:
			if (top == -1) printf("-1\n");
			else printf("%d\n", stack[top]);
			break;
		}
	}
	return 0;
}