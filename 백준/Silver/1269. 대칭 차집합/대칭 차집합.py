import sys
input = sys.stdin.readline

input()
a = set()
a.update(map(int, input().split()))
b = set()
b.update(map(int, input().split()))
print(len(a.difference(b)) + len(b.difference(a)))