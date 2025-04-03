import re
import sys
input = sys.stdin.readline

s = input().strip()
print(len(re.findall(r"(?=(JOI))", s)))
print(len(re.findall(r"(?=(IOI))", s)))