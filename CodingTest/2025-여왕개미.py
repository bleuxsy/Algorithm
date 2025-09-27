from collections import deque


# [1] 마을 건설
def make_town(house, dir):
    house = house + dir
    house.sort()

    return house


# [2] 개미집 건설
def make_house(house, p):
    house.append(p)

    return house


# [3] 개미집 철거
def del_house(house, q):
    # 이미 철거된 상태거나, 아직 지어지지 않은 경우는 입력으로 들어오지 않음.

    house.pop(q)

    return house


def dfs(L, idx, total):
    global res

    if L == r - 1:
        if idx < len(house) - 1:
            total += house[-1] - house[idx]

        if res > total:
            res = total
            return
    else:
        for i in range(idx + 1, len(house)):
            if i - idx == 0:
                dfs(L + 1, i + 1, total)
            else:
                cnt = house[i] - house[idx]
                if total < cnt:
                    total = cnt
                dfs(L + 1, i + 1, total)


# [4] 개미집 정찰
def go_ant():
    global res

    res = sum(house)

    dfs(0, 1, 0)
    print(res)


####################
if __name__ == "__main__":
    Q = int(input())
    time = deque()
    house = [0]
    for i in range(Q):

        p, q, r = 0, 0, 0
        cmd = list(map(int, input().split()))
        if cmd[0] == 100:
            house = make_town(house, cmd[2:])
        elif cmd[0] == 200:
            p = cmd[1]
            house = make_house(house, p)
        elif cmd[0] == 300:
            q = cmd[1]
            house = del_house(house, q)

        else:
            r = cmd[1]
            go_ant()
