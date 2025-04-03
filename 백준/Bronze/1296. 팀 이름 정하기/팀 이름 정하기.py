import sys
input = sys.stdin.readline

name = input().strip()
name_score = [name.count(c) for c in "LOVE"]
teams = [input().strip() for _ in range(int(input()))]
max_score = -1
result = teams[0]

def get(team_name):
	l = name_score[0] + team_name.count('L')
	o = name_score[1] + team_name.count('O')
	v = name_score[2] + team_name.count('V')
	e = name_score[3] + team_name.count('E')
	return ((l + o) * (l + v) * (l + e) * (o + v) * (o + e) * (v + e)) % 100

for team in teams:
	team_score = get(team)
	if team_score > max_score:
		max_score = team_score
		result = team
	elif team_score == max_score:
		result = team if team < result else result
print(result)