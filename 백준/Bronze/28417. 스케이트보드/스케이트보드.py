import sys
input = sys.stdin.readline

people = []
for _ in range(int(input())):
	score = list(map(int, input().split()))
	run_score = max(score[0], score[1])
	act_score = sum(sorted(score[2:], reverse=True)[:2])
	people.append(run_score + act_score)
print(max(people))