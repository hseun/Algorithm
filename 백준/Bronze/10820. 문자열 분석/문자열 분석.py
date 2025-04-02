import re
import sys
input = sys.stdin.readline

patterns = [
    re.compile(r"[A-Z0-9\s]"),
    re.compile(r"[a-z0-9\s]"),
    re.compile(r"[a-zA-Z\s]"),
    re.compile(r"[a-zA-Z0-9]")
]

while True:
    result = []
    s = input()[:-1]
    if s == "":
        break
    for pattern in patterns:
        result.append(len(re.sub(pattern, "", s)))
    print(*result)