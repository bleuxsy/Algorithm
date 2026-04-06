import sys

sys.stdin = open("input.txt", "r")

# [1] 마을 건설
def make_town(lst):
    house[0] = 0   # 여왕 개미 집
    for i, x in enumerate(lst, start=1):
        house[i] = x


# [2] 개미집 건설
def make_house(nxt, p):
    house[nxt] = p


# [3] 개미집 철거
def del_house(q):
    house.pop(q)


def can(pos, r, T):
    n = len(pos)
    used = 0
    i = 1

    while i < n:
        used += 1
        if used > r:
            return False

        start = pos[i]
        limit = start + T

        j = i
        while j < n and pos[j] <= limit:
            j += 1

        i = j

    return True


# [4] 개미집 정찰
def go_ant(r):
    pos = sorted(house.values())

    left, right = 0, pos[-1] - pos[0]
    ans = right

    while left <= right:
        mid = (left + right) // 2

        if can(pos, r, mid):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1

    print(ans)


####################
if __name__ == "__main__":
    Q = int(input())
    house = {}

    nxt = 1
    for _ in range(Q):
        cmd = list(map(int, input().split()))

        if cmd[0] == 100:
            N = cmd[1]
            make_town(cmd[2:])
            nxt = N + 1

        elif cmd[0] == 200:
            p = cmd[1]
            make_house(nxt, p)
            nxt += 1

        elif cmd[0] == 300:
            q = cmd[1]
            del_house(q)

        else:   # 400
            r = cmd[1]
            go_ant(r)