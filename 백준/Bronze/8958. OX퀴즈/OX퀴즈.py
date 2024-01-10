n = int(input())
for i in range(n):
    score = 0
    result = list(input())
    count = 0
    for j in result:
        if j == 'O':
            count += 1
            score += count
        else:
            count = 0
    print(score)