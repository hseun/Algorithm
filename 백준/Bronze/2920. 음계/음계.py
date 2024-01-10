num = list(map(int, input().split()))
count = 0
for i in range(1, 9):
    if i == num[count]:
        count += 1
    else:
        break
if count == 8:
    print("ascending")
else:
    count = 0
    for i in range(8, 0, -1):
        if i == num[count]:
            count += 1
        else:
            break
    if count == 8:
        print("descending")
    else:
        print("mixed")