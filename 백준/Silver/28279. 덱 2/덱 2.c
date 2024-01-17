#include <stdio.h>

int main(void) {
	int command, front = 0, rear = 0, max = 1000000;
	int que[1000000], n, temp;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &command);
		switch (command) {
		case 1:
			scanf("%d", &temp);
			rear = (rear + 1) % max;
			que[rear] = temp;
			break;
		case 2:
			scanf("%d", &temp);
			que[front] = temp;
			front = (front - 1 + max) % max;
			break;
		case 3:
			if (front == rear)
				printf("-1\n");
			else {
				printf("%d\n", que[rear]);
				rear = (rear - 1 + max) % max;
			}
			break;
		case 4:
			if (front == rear)
				printf("-1\n");
			else {
				front = (front + 1) % max;
				printf("%d\n", que[front]);
			}
			break;
		case 5:
			printf("%d\n", (rear - front + max) % max);
			break;
		case 6:
			if (front == rear)
				printf("1\n");
			else
				printf("0\n");
			break;
		case 7:
			if (front == rear)
				printf("-1\n");
			else
				printf("%d\n", que[rear]);
			break;
		case 8:
			if (front == rear)
				printf("-1\n");
			else
				printf("%d\n", que[(front + 1) % max]);
			break;
		}
	}
	return 0;
}