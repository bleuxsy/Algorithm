def solution(id_list, report, k):
    answer = []
    suspends = []
    dic = {}
    ids = [0] * len(id_list)
    check = [False] * len(id_list)
    result = [0] * len(id_list)
    for i in report:
        a, b = i.split(" ")
        if a not in dic:
            dic[a] = []
        if b not in dic[a]:
            dic[a].append(b)
    for key, users in dic.items():
        for user in users:
            ids[id_list.index(user)] += 1
    for idx, cons in enumerate(ids):
        if cons >= k:
            check[idx] = True
    for key, users in dic.items():
        for user in users:
            if check[id_list.index(user)]:
                result[id_list.index(key)] += 1

    return result