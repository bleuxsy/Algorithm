def solution(n, costs):
    answer = 0
    
    #크루스칼 알고리즘
    costs.sort(key = lambda x: x[2])
    link = set([costs[0][0]])
    while len(link) != n:
        for c in costs:
            if c[0] in link and c[1] in link:
                continue
            if c[0] in link or c[1] in link:
                link.update([c[0], c[1]])
                answer += c[2]
                break
    return answer