import sys
input = sys.stdin.readline

s = input().strip()
counts = 0
words = ["c=", "c-", "d-", "lj", "nj", "s=", "z="]

word_index = s.find("dz=")
while word_index != -1:
    counts += 1
    s = s[:word_index] + " " + s[word_index + 3:]
    word_index = s.find("dz=")

for word in words:
    word_index = s.find(word)
    while word_index != -1:
        counts += 1
        s = s[:word_index] + " " + s[word_index + 2:]
        word_index = s.find(word)
counts = counts + sum([len(word) for word in s.split()])
print(counts)