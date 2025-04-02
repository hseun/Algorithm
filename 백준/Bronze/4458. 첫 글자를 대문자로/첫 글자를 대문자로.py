import sys
input = sys.stdin.readline

words = [input().strip() for _ in range(int(input()))]
for word in words:
    print(word.replace(word[0], word[0].upper(), 1))