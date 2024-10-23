import sys
input = sys.stdin.readline

for _ in range(int(input())):
    words = input().split()
    if sorted(words[0]) == sorted(words[1]):
        print(f"{words[0]} & {words[1]} are anagrams.")
    else:
        print(f"{words[0]} & {words[1]} are NOT anagrams.")