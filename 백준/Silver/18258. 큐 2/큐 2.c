#include <stdio.h>

int main(void) {
	int n, que[2000000], rear = -1, front = -1, temp;
	char command[10];
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%s", command);
		switch (command[0]) {
		case 'p':
			if (command[1] == 'u') {
				scanf("%d", &temp);
				que[++rear] = temp;
			}
			else {
				if (rear == front)
					printf("-1\n");
				else
					printf("%d\n", que[++front]);
			}
			break;
		case 's':
			printf("%d\n", rear - front);
			break;
		case 'e':
			if (rear == front)
				printf("1\n");
			else
				printf("0\n");
			break;
		case 'f':
			if (rear == front)
				printf("-1\n");
			else
				printf("%d\n", que[front + 1]);
			break;
		case 'b':
			if (rear == front)
				printf("-1\n");
			else
				printf("%d\n", que[rear]);
			break;
		}
	}
	return 0;
}