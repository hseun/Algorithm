n = int(input())
shirts = list(map(int, input().split()))
shirt_order = 0
t, p = map(int, input().split())

for shirt in shirts:
    shirt_order += shirt // t if shirt % t == 0 else shirt // t + 1
print(shirt_order)
print(n // p, n % p)