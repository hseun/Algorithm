engs = 'bcdefghijklmnopqrstuvwxyz'
s = ''
while True:
    try:
        s += input()
    except:
        break

result = 'a'
count = s.count('a')

for eng in engs:
    engCount = s.count(eng)
    if engCount == count:
        result += eng
    elif engCount > count:
        count = engCount
        result = eng

print(result)