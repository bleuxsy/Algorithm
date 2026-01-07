T = int(input())
for _ in range(T):
    W = list(input().strip())
    ## 양쪽 개행문자 제거
    K = int(input())
    cnt = {}
    flag = 0
    for i, ch in enumerate(W):
        if ch not in cnt:
            cnt[ch] = []
        cnt[ch].append(i)

    min_len = 100000
    max_len = 0

    for ch in cnt:
        if len(cnt[ch]) >= K:
            for i in range(len(cnt[ch]) - K +1):
                length = cnt[ch][i+K-1] - cnt[ch][i] +1
                min_len = min(min_len , length)
                max_len = max(max_len, length)

    if min_len == 100000:
        print(-1)
    else:
        print(min_len, max_len)

    #     if len(cnt[W[w]]) == K:
    #         dis = cnt[W[w]][1] - cnt[W[w]][0]
    #         cnt[W[w]].append(dis)
    # sorted_item = sorted(cnt.items(), key= lambda x : x[1][2])
    #
    # first_key = list(sorted_item.keys())
    #
