def solution(name, yearning, photo):
    answer = []
    for p in photo:
        score = sum([yearning[name.index(a)] for a in p if a in name])
        answer.append(score)
    return answer