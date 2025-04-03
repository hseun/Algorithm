import sys
input = sys.stdin.readline

for _ in range(int(input())):
    num = input().strip()
    reverse_num = ''.join(list(reversed(num)))
    result = str(int(num) + int(reverse_num))
    result_len = len(result)
    right = ''
    left = result[:result_len // 2]
    if result_len % 2 == 0:
        right = ''.join(list(reversed(result[result_len // 2:])))
    else:
        right = ''.join(list(reversed(result[result_len // 2 + 1:])))
    print("YES" if left == right else "NO")