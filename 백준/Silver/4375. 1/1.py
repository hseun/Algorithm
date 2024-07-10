while True:
    try:
        n = int(input())
        count = 1
        while int('1' * count) % n != 0:
            count += 1
        print(count)
    except:
        break