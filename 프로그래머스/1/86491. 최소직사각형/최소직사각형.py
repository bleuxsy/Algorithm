def solution(sizes):
    answer = 0
    w = []
    h = []
    for i, j in sizes:
        if i >= j : 
            w.append(i)
            h.append(j)
        else:
            w.append(j)
            h.append(i)
    print(max(w))
    print(max(h))
    answer = max(w) * max(h)
    return answer