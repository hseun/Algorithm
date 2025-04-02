import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pokemon = [""]
pokemon_index = {}
for i in range(n):
    name = input().strip()
    pokemon.append(name)
    pokemon_index[name] = i + 1
for _ in range(m):
    q = input().strip()
    if q.isdigit():
        print(pokemon[int(q)])
    else:
        print(pokemon_index[q])