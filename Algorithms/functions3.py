import sys
from collections import deque

sys.stdin = open("input.txt", "r")

EAST, WEST, SOUTH, NORTH, TOP = 0, 1, 2, 3, 4


def convert_exit(org_ex, org_ey, ed, cube_sx, cube_sy, M):
    # org_ex, org_ey는 평면에서 시간의 벽(3) 칸 좌표
    if ed == 3:   # 북쪽 출구
        c_off = org_ey - cube_sy
        return NORTH, M - 1, M - c_off - 1
    elif ed == 2: # 남쪽 출구
        c_off = org_ey - cube_sy
        return SOUTH, M - 1, c_off
    elif ed == 1: # 서쪽 출구
        r_off = org_ex - cube_sx
        return WEST, M - 1, r_off
    else:         # 동쪽 출구
        r_off = org_ex - cube_sx
        return EAST, M - 1, M - r_off - 1


def move(face, r, c):
    nxt = []

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < M and 0 <= nc < M:
            nxt.append((face, nr, nc))

    transitions = []

    if face == TOP:
        if r == 0:
            transitions.append((NORTH, 0, M - c - 1))
        if r == M - 1:
            transitions.append((SOUTH, 0, c))
        if c == 0:
            transitions.append((WEST, 0, r))
        if c == M - 1:
            transitions.append((EAST, 0, M - r - 1))

    elif face == NORTH:
        if r == 0:
            transitions.append((TOP, 0, M - c - 1))
        if c == M - 1:
            transitions.append((WEST, r, 0))
        if c == 0:
            transitions.append((EAST, r, M - 1))

    elif face == SOUTH:
        if r == 0:
            transitions.append((TOP, M - 1, c))
        if c == 0:
            transitions.append((WEST, r, M - 1))
        if c == M - 1:
            transitions.append((EAST, r, 0))

    elif face == WEST:
        if r == 0:
            transitions.append((TOP, c, 0))
        if c == 0:
            transitions.append((NORTH, r, M - 1))
        if c == M - 1:
            transitions.append((SOUTH, r, 0))

    elif face == EAST:
        if r == 0:
            transitions.append((TOP, M - c - 1, M - 1))
        if c == M - 1:
            transitions.append((NORTH, r, 0))
        if c == 0:
            transitions.append((SOUTH, r, M - 1))

    nxt.extend(transitions)
    return nxt


def build_anomaly_blocks():
    anomaly_blocks = [[float('inf')] * N for _ in range(N)]

    anomaly_dr = [0, 0, 1, -1]  # 동 서 남 북
    anomaly_dc = [1, -1, 0, 0]

    for r, c, d, v in strange:
        if grid[r][c] != 4:
            anomaly_blocks[r][c] = min(anomaly_blocks[r][c], 0)

        time_step = v
        nr, nc = r, c

        while True:
            nr += anomaly_dr[d]
            nc += anomaly_dc[d]

            if not (0 <= nr < N and 0 <= nc < N):
                break
            if grid[nr][nc] in [1, 4]:
                break

            anomaly_blocks[nr][nc] = min(anomaly_blocks[nr][nc], time_step)
            time_step += v

    return anomaly_blocks


def bfs_grid(start_time, start_x, start_y):
    q = deque([(start_time, start_x, start_y)])
    visited_grid = [[float('inf')] * N for _ in range(N)]
    visited_grid[start_x][start_y] = start_time

    while q:
        time, x, y = q.popleft()

        if grid[x][y] == 4:
            return time

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            nt = time + 1

            if not (0 <= nx < N and 0 <= ny < N):
                continue
            if grid[nx][ny] in [1, 3]:
                continue
            if nt >= anomaly_blocks[nx][ny]:
                continue
            if nt >= visited_grid[nx][ny]:
                continue

            visited_grid[nx][ny] = nt
            q.append((nt, nx, ny))

    return -1


if __name__ == "__main__":
    N, M, F = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    cube = []
    for _ in range(5):
        face = [list(map(int, input().split())) for _ in range(M)]
        cube.append(face)

    strange = [tuple(map(int, input().split())) for _ in range(F)]

    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # 시작점 찾기
    sx = sy = -1
    for i in range(M):
        for j in range(M):
            if cube[TOP][i][j] == 2:
                sx, sy = i, j
                cube[TOP][i][j] = 0
                break
        if sx != -1:
            break

    # 시간의 벽 좌상단 찾기
    cube_sx = cube_sy = -1
    for i in range(N):
        if 3 in grid[i]:
            cube_sx = i
            cube_sy = grid[i].index(3)
            break

    # 큐브 출구 찾기
    org_ex = org_ey = -1
    out_x = out_y = -1
    ed = -1

    # 북
    if cube_sx > 0:
        for c_off in range(M):
            if grid[cube_sx - 1][cube_sy + c_off] == 0:
                out_x, out_y = cube_sx - 1, cube_sy + c_off
                org_ex, org_ey = cube_sx, cube_sy + c_off
                ed = 3
                break

    # 남
    if ed == -1 and cube_sx + M < N:
        for c_off in range(M):
            if grid[cube_sx + M][cube_sy + c_off] == 0:
                out_x, out_y = cube_sx + M, cube_sy + c_off
                org_ex, org_ey = cube_sx + M - 1, cube_sy + c_off
                ed = 2
                break

    # 서
    if ed == -1 and cube_sy > 0:
        for r_off in range(M):
            if grid[cube_sx + r_off][cube_sy - 1] == 0:
                out_x, out_y = cube_sx + r_off, cube_sy - 1
                org_ex, org_ey = cube_sx + r_off, cube_sy
                ed = 1
                break

    # 동
    if ed == -1 and cube_sy + M < N:
        for r_off in range(M):
            if grid[cube_sx + r_off][cube_sy + M] == 0:
                out_x, out_y = cube_sx + r_off, cube_sy + M
                org_ex, org_ey = cube_sx + r_off, cube_sy + M - 1
                ed = 0
                break

    if ed == -1:
        print(-1)
        sys.exit()

    goal_face, goal_r, goal_c = convert_exit(org_ex, org_ey, ed, cube_sx, cube_sy, M)

    # 1) 큐브 BFS
    visited_cube = [[[False] * M for _ in range(M)] for _ in range(5)]
    q = deque([(0, TOP, sx, sy)])
    visited_cube[TOP][sx][sy] = True

    time_to_exit_wall = -1
    while q:
        time, face, r, c = q.popleft()

        if (face, r, c) == (goal_face, goal_r, goal_c):
            time_to_exit_wall = time + 1
            break

        for nf, nr, nc in move(face, r, c):
            if not (0 <= nr < M and 0 <= nc < M):
                continue
            if visited_cube[nf][nr][nc]:
                continue
            if cube[nf][nr][nc] == 1:
                continue

            visited_cube[nf][nr][nc] = True
            q.append((time + 1, nf, nr, nc))

    if time_to_exit_wall == -1:
        print(-1)
        sys.exit()

    # 2) 이상현상 전처리
    anomaly_blocks = build_anomaly_blocks()

    # 시작 바깥칸 자체가 이미 막혀 있으면 불가
    if time_to_exit_wall >= anomaly_blocks[out_x][out_y]:
        print(-1)
        sys.exit()

    # 3) 평면 BFS
    answer = bfs_grid(time_to_exit_wall, out_x, out_y)
    print(answer)