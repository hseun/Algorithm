import sys

input = sys.stdin.readline

input()
card_set = set()
card_set.update(list(map(int, input().split())))
input()
for n in list(map(int, input().split())):
    print(1 if n in card_set else 0, end=" ")