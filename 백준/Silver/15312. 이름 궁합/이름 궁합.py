import sys
input = sys.stdin.readline

write_count = {"A": 3, "B": 2, "C": 1, "D": 2, "E": 3, "F": 3, "G": 2, "H": 3, "I": 3, "J": 2, "K": 2, "L": 1, "M": 2, "N": 2, "O": 1, "P": 2, "Q": 2, "R": 2, "S": 1, "T": 2, "U": 1, "V": 1, "W": 1, "X": 2, "Y": 2, "Z": 1}
score = []
a = input().strip()
b = input().strip()
for i in range(len(a)):
    score.append(write_count[a[i]])
    score.append(write_count[b[i]])
while len(score) > 2:
    score = [(score[i] + score[i + 1]) % 10 for i in range(len(score) - 1)]
print("%02d" % (score[0] * 10 + score[1]))