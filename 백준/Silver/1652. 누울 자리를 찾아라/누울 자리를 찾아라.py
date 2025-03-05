import sys
input = sys.stdin.readline

n = int(input())
result_row = 0
result_column = 0
rooms = [input().strip() for _ in range(n)]

for i in range(n):
    row_room = rooms[i].split("X")
    result_row += sum([True for room in row_room if ".." in room])
    column_room = ''.join([rooms[j][i] for j in range(n)]).split("X")
    result_column += sum([True for room in column_room if ".." in room])
print(result_row, result_column)