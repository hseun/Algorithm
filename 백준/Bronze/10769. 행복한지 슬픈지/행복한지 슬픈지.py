import sys
input = sys.stdin.readline

message = input().strip()
happy = message.count(":-)")
sad = message.count(":-(")
if happy + sad == 0:
    print("none")
elif happy > sad:
    print("happy")
elif sad > happy:
    print("sad")
else:
    print("unsure")