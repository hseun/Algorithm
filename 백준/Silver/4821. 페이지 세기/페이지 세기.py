import sys
input = sys.stdin.readline

while True:
    page_set = set()
    paper = int(input())
    if paper == 0: break
    pages = input().split(',')
    for page in pages:
        if '-' not in page:
            p = int(page)
            if p <= paper:
                page_set.add(p)
            continue
        low, high = map(int, page.split('-'))
        high = min(high, paper)
        page_set.update(range(low, high + 1))
    print(len(page_set))