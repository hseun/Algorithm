from queue import Queue
import sys

input = sys.stdin.readline
que = Queue()

for _ in range(int(input())):
    commands = input().split()
    if commands[0] == "push":
        que.put(commands[1])
    elif commands[0] == "pop":
        print(que.get() if que.qsize() != 0 else -1)
    elif commands[0] == "size":
        print(que.qsize())
    elif commands[0] == "empty":
        print(1 if que.qsize() == 0 else 0)
    elif commands[0] == "front":
        print(que.queue[0] if que.qsize() != 0 else -1)
    else:
        print(que.queue[-1] if que.qsize() != 0 else -1)