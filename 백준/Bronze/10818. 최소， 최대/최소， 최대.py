n = int(input())
li = input().split()
Min = 1000000
Max = -1000000
for i in li:
    i = int(i)
    if i > Max:
        Max = i
    if i < Min:
        Min = i
print(Min, Max)