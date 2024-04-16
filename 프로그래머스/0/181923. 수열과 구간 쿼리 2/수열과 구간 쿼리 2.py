def solution(arr, queries):
    answer = []
    for q in queries:
        array = [arr[i] for i in range(len(arr)) if q[0] <= i and i <= q[1] and arr[i] > q[2]]
        if len(array) == 0:
            answer.append(-1)
        else:
            answer.append(min(array))
    return answer