def solution(arr, queries):
    for q in queries:
        arr = arr[:q[0]] + [arr[i] + 1 if i % q[2] == 0 else arr[i] for i in range(q[0], q[1] + 1)] + arr[q[1] + 1:]
    return arr