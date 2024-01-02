n = int(input())
for _ in range(n):
    nums = list(map(int, input().split()))
    nums = [a for a in nums if a % 2 == 0]
    Min = 100
    Sum = 0
    for i in nums:
        Sum += i
        if i < Min:
            Min = i
    print(Sum, Min)