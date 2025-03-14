import sys
input = sys.stdin.readline

code = {
    "D": 1, "E": 2, "F": 3, "G": 4, "H": 5, "I": 6, "J": 7, "K": 8, "L": 9,
    "M": 10, "N": 11, "O": 12, "P": 13, "Q": 14, "R": 15, "S": 16, "T": 17,
    "U": 18, "V": 19, "W": 20, "X": 21, "Y": 22, "Z": 23, "A": 24, "B": 25, "C": 26
}

alpha = {
    1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H", 9: "I",
    10: "J", 11: "K", 12: "L", 13: "M", 14: "N", 15: "O", 16: "P", 17: "Q",
    18: "R", 19: "S", 20: "T", 21: "U", 22: "V", 23: "W", 24: "X", 25: "Y", 26: "Z"
}

string = input().strip()
for s in string:
    print(alpha[code[s]], end="")