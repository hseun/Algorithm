#include <stdio.h>

int stack[100000];
int top = -1;

void push(int item) {
	stack[++top] = item;
}
int pop() {
	if (top == -1)
		return -1;
	else
		return stack[top--];
}
int size() {
	return top + 1;
}
int empty() {
	return top == -1;
}
int fnTop() {
	if (top == -1)
		return -1;
	else
		return stack[top];
}
int main(void) {
	int n, item;
	char str[10];
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%s", str);
		switch (str[0]) {
		case 'p':
			if (str[1] == 'u') {
				scanf("%d", &item);
				push(item);
			}
			else
				printf("%d\n", pop());
			break;
		case 's':
			printf("%d\n", size());
			break;
		case 'e':
			printf("%d\n", empty());
			break;
		case 't':
			printf("%d\n", fnTop());
			break;
		}
	}
	return 0;
}