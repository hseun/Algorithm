import sys
input = sys.stdin.readline

while True:
    page_set = set()
    paper = int(input())
    if paper == 0: break
    pages = input().split(',')
    for page in pages:
        if '-' not in page:
            if int(page) <= paper:
                page_set.add(int(page))
            continue
        low, high = map(int, page.split('-'))
        high = min(high, paper)
        for i in range(low, high + 1):
            page_set.add(i)
    print(len(page_set))