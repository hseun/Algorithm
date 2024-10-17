import sys
input = sys.stdin.readline

books = [input() for _ in range(int(input()))]
book_set = set(books)
result = []
result_count = 0
for book in book_set:
    book_count = books.count(book)
    if book_count > result_count:
        result_count = book_count
        result = [book]
    elif book_count == result_count:
        result += [book]
print(sorted(result)[0])