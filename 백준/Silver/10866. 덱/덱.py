from collections import deque
import sys
input = sys.stdin.readline

que = deque()
for _ in range(int(input())):
    order = input().split()
    if order[0] == "push_front":
        que.appendleft(order[1])
    elif order[0] == "push_back":
        que.append(order[1])
    elif order[0] == "pop_front":
        if len(que):
            print(que.popleft())
        else:
            print("-1")
    elif order[0] == "pop_back":
        if len(que):
            print(que.pop())
        else:
            print("-1")
    elif order[0] == "size":
        print(len(que))
    elif order[0] == "empty":
        print("0" if len(que) else "1")
    elif order[0] == "front":
        print(que[0] if len(que) else "-1")
    else:
        print(que[-1] if len(que) else "-1")