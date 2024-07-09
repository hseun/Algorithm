t = int(input())
for _ in range(t):
    n = int(input())
    rooms = [True] * (n + 1)
    for i in range(2, n + 1):
        rooms = [not rooms[a] if a % i == 0 else rooms[a] for a in range(len(rooms))]
    del rooms[0]
    print(rooms.count(True))