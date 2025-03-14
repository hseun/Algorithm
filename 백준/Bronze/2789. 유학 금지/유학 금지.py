import sys
import re
input = sys.stdin.readline

s = input().strip()
result = re.sub("[CAMBRIDGE]", "", s)
print(result)