fbi = []
for i in range(5):
    name = input()
    if name.find("FBI") != -1:
        fbi.append(i + 1)
if len(fbi) > 0:
    for i in fbi:
        print(i, end=" ")
else:
    print("HE GOT AWAY!")
