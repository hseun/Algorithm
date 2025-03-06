import sys
input = sys.stdin.readline

for _ in range(int(input())):
    speaks = input().split()
    animals = set()
    while True:
        animal = input().strip()
        if animal == "what does the fox say?":
            break
        animals.add(animal.split()[-1])
    speaks = [speak for speak in speaks if speak not in animals]
    print(' '.join(speaks))