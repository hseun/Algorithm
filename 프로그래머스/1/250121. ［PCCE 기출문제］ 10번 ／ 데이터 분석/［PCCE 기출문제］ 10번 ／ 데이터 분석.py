def solution(data, ext, val_ext, sort_by):
    li = ['code', 'date', 'maximum', 'remain']
    answer = [data[i] for i in range(len(data)) if data[i][li.index(ext)] < val_ext]
    return sorted(answer, key=lambda x: x[li.index(sort_by)])