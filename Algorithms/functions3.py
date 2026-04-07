import sys
sys.stdin = open("input.txt", "r")

exit_dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]   # 북 동 남 서


def myprint(lst):
    for l in lst:
        print(*l)
    print()


def can_move(x, y, sd):
    # sd: 0 남, 1 서회전후하강, 2 동회전후하강

    # 남쪽으로 한 칸
    if sd == 0:
        cells = [
            (x + 1, y - 1),
            (x + 2, y),
            (x + 1, y + 1),
        ]

    # 서쪽으로 회전 후 아래
    elif sd == 1:
        cells = [
            (x - 1, y - 1),
            (x,     y - 2),
            (x + 1, y - 1),
            (x + 1, y - 2),
            (x + 2, y - 1),
        ]

    # 동쪽으로 회전 후 아래
    else:
        cells = [
            (x - 1, y + 1),
            (x,     y + 2),
            (x + 1, y + 1),
            (x + 1, y + 2),
            (x + 2, y + 1),
        ]

    for nx, ny in cells:
        if not (0 <= nx < R + 3 and 0 <= ny < C):
            return False
        if grid[nx][ny] != 0:
            return False

    return True


def move_golem(org_c, org_d):
    global grid

    x = 1
    y = org_c
    exit_d = org_d

    while True:
        if can_move(x, y, 0):          # 남
            x += 1

        elif can_move(x, y, 1):        # 서회전 + 하강
            x += 1
            y -= 1
            exit_d = (exit_d + 3) % 4

        elif can_move(x, y, 2):        # 동회전 + 하강
            x += 1
            y += 1
            exit_d = (exit_d + 1) % 4

        else:
            break

    # 숲 밖에 걸친 경우
    if x < 4:
        grid = [[0] * C for _ in range(R + 3)]
        return -1, -1, -1

    return x, y, exit_d


def place_golem(x, y, idx):
    grid[x][y] = idx
    grid[x - 1][y] = idx
    grid[x + 1][y] = idx
    grid[x][y - 1] = idx
    grid[x][y + 1] = idx


def escape(x, y, idx):
    global visited

    max_r = x

    for dx, dy in exit_dir:
        nx, ny = x + dx, y + dy

        if not (3 <= nx < R + 3 and 0 <= ny < C):
            continue
        if visited[nx][ny]:
            continue

        nidx = grid[nx][ny]

        # 같은 골렘 내부 이동
        if nidx == idx:
            visited[nx][ny] = True
            max_r = max(max_r, escape(nx, ny, idx))
            visited[nx][ny] = False

        # 현재 칸이 출구라면 다른 골렘으로 이동 가능
        elif golem[idx] == (x, y) and nidx != 0:
            visited[nx][ny] = True
            max_r = max(max_r, escape(nx, ny, nidx))
            visited[nx][ny] = False

    return max_r


if __name__ == "__main__":
    R, C, K = map(int, input().split())

    grid = [[0] * C for _ in range(R + 3)]
    golem = {i: (0, 0) for i in range(1, K + 1)}
    answer = 0

    for idx in range(1, K + 1):
        c, d = map(int, input().split())

        golem_x, golem_y, golem_d = move_golem(c - 1, d)

        # 숲 밖 걸침 -> 초기화 후 이번 골렘은 배치하지 않음
        if golem_x == -1:
            golem = {i: (0, 0) for i in range(1, K + 1)}
            continue

        # 출구 좌표 저장
        ex, ey = exit_dir[golem_d]
        golem[idx] = (golem_x + ex, golem_y + ey)

        # 골렘 배치
        place_golem(golem_x, golem_y, idx)

        # 정령 이동
        visited = [[False] * C for _ in range(R + 3)]
        visited[golem_x][golem_y] = True

        res = escape(golem_x, golem_y, idx) - 2
        answer += res

    print(answer)