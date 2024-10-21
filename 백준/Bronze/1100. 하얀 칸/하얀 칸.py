import sys
input = sys.stdin.readline

chess_count = 0
for i in range(8):
    chess = input()
    chess_count += len([a for a in range(len(chess)) if chess[a] == 'F' and a % 2 == i % 2])
print(chess_count)