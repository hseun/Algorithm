n = int(input())
words = set(input() for _ in range(n))
words = sorted(words)
words.sort(key=len)
for i in words:
    print(i)