import sys
input = sys.stdin.readline

document = input().strip()
search_word = input().strip()
print(document.count(search_word))