from collections import  deque
import sys

input = sys.stdin.readline

def action_command(command):
    is_reversed = False
    for c in command:
        if c == 'R':
            is_reversed = not is_reversed
        else:
            if len(nums) == 0: return 'error'
            if is_reversed:
                nums.pop()
            else:
                nums.popleft()
    if len(nums) == 0: return '[]'
    return f'[{','.join(nums if not is_reversed else reversed(nums))}]'

for _ in range(int(input())):
    commands = input().strip()
    n = int(input())
    arr = input().strip()
    nums = []
    if n != 0: nums = deque(arr.strip()[1:-1].split(','))
    print(action_command(commands))