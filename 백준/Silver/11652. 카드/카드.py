import sys
from collections import Counter
input = sys.stdin.readline

cards = [int(input()) for _ in range(int(input()))]

card_counter = Counter(cards)
max_counter = max(card_counter.values())
max_card = [card for card, counter in card_counter.items() if counter == max_counter]
print(min(max_card))