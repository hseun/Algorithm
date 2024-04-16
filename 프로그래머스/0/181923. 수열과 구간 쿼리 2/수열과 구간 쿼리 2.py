def solution(arr, queries):
    answer = [-1] * len(queries)
    for i in range(len(queries)):
        s, e, k = queries[i][0], queries[i][1], queries[i][2]
        temp = [n for n in arr[s:e+1] if n > k]
        if len(temp) > 0:
            answer[i] = min(temp)
    return answer