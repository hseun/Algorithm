n, b = map(int, input().split())
code = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = ''
while n:
    result += str(code[n % b])
    n //= b
print(result[::-1])