import sys
import re
input = sys.stdin.readline

speak = input().strip()
speak = re.sub(r"pi|ka|chu", "", speak)
print("YES" if not speak else "NO")