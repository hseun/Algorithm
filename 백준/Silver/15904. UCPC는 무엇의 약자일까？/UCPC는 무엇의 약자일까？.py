import re
import sys
input = sys.stdin.readline

s = input().strip()
want = iter(['U', 'C', 'P', 'C'])
s = iter(re.sub(r"[a-z\s]", "", s))
print("I love UCPC" if all(a in s for a in want) else "I hate UCPC")