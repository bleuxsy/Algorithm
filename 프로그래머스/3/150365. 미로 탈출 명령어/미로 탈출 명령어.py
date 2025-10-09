import sys

sys.setrecursionlimit(2600)

global maxR, maxC, endR, endC, maxDepth

dirs = [
    ['d', 1, 0],  # d ↓ dR +1  dC 0
    ['l', 0, -1],  # l ← dR  0  dC -1
    ['r', 0, 1],  # r → dR  0  dC +1
    ['u', -1, 0]  # u ↑ dR -1  dC 0
]

def solution(n, m, x, y, r, c, k):
    global maxR, maxC, endR, endC, maxDepth

    maxR, maxC, endR, endC, maxDepth = n, m, r, c, k
    distance = abs(x - r) + abs(y - c)

    if distance > maxDepth:
        return 'impossible'

    if distance % 2 is not maxDepth % 2:
        return 'impossible'

    answer = dfs(x, y, '', 0)

    if answer is None:
        answer = 'impossible'

    return answer

def dfs(sR, sC, path, currentDepth):
    global maxR, maxC, endR, endC, maxDepth

    if currentDepth == maxDepth:
        if sR == endR and sC == endC:
            return path
    else:
        for prc in dirs:
            p, dR, dC = prc
            dstR = sR + dR
            dstC = sC + dC
            if 1 <= dstR <= maxR and 1 <= dstC <= maxC:
                distance = abs(dstR - endR) + abs(dstC - endC)

                if distance > maxDepth - (currentDepth + 1):
                    continue

                rtn = dfs(dstR, dstC, path + p, currentDepth + 1)

                if rtn is not None:
                    return rtn