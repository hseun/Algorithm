result = int(input()) * int(input()) * int(input())
result = list(str(result))
for i in range(10):
    print(result.count(str(i)))