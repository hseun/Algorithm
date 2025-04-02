from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
vote = Counter(list(input().strip()))
if vote['A'] == vote['B']:
    print("Tie")
else:
    print("A" if vote['A'] > vote['B'] else "B")