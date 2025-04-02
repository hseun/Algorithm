import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, word = input().strip().split()
    word = list(word)
    del word[int(n) - 1]
    print(''.join(word))