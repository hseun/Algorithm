import sys
from collections import deque

input = sys.stdin.readline

city_count, street_count, road_info, start_city = map(int, input().split())
cities = [[] for _ in range(city_count + 1)]
for _ in range(street_count):
    start, end = map(int, input().split())
    cities[start].append(end)

que = deque()
visited_city = set()
target_city = []

que.append((start_city, 0))
visited_city.add(start_city)

while que:
    current_city, far = que.popleft()
    if far == road_info:
        target_city.append(current_city)
    for next_city in cities[current_city]:
        if next_city not in visited_city:
            que.append((next_city, far + 1))
            visited_city.add(next_city)

if len(target_city) == 0:
    print(-1)
else:
    [print(city) for city in sorted(target_city)]