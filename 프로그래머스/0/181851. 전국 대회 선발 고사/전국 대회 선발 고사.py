def solution(rank, attendance):
    person = [[rank[i], i] for i in range(len(rank)) if attendance[i]]
    person.sort(key=lambda x: x[0])
    return person[0][1] * 10000 + person[1][1] * 100 + person[2][1]