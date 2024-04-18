def solution(arr, k):
    arr = sorted(list(set(arr)), key=lambda x: arr.index(x))
    return arr[:k] if len(arr) >= k else arr + [-1] * (k - len(arr))