def solution(clothes):
    answer = 1
    num = 0
    num2 = 1
    kinds = {}
    for i in range(len(clothes)):
        kind = clothes[i][1]
        item = clothes[i][0]
        if kind in kinds:
            kinds[kind].append(item)
        else:
            kinds[kind] = [item]
    for kind in kinds:
        answer *= (len(kinds[kind]) + 1)
    return answer-1