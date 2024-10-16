import sys
input = sys.stdin.readline

s = input().rstrip()
words = sorted([s[a:] for a in range(len(s))])
[print(word) for word in words]