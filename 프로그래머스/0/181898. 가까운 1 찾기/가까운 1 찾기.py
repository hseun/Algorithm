def solution(arr, idx):
    arr = "".join(list(map(str, arr)))
    return arr.find("1", idx)