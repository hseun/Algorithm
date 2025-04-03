import sys
input = sys.stdin.readline

for _ in range(int(input())):
    max_price = 0
    max_name = ''
    for _ in range(int(input())):
        price, name = input().strip().split()
        if int(price) > max_price:
            max_price = int(price)
            max_name = name
    print(max_name)