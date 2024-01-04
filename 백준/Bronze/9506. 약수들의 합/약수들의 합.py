n = int(input())
while n != -1:
    num = [a for a in range(1, n) if n % a == 0]
    if sum(num) == n:
        print(n, "=", ' + '.join(str(i) for i in num), sep=" ")
    else:
        print(n, "is NOT perfect.")
    n = int(input())