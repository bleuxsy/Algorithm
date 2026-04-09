import sys
from collections import deque

# 전역 변수 정의
n, m, f = 0, 0, 0
space_grid = None
views = None
anomalies = None

# 면(face) 인덱스 상수 정의 (가독성을 위해)
# views 리스트의 인덱스와 매핑됩니다.
EAST, WEST, SOUTH, NORTH, TOP = 0, 1, 2, 3, 4


def read_input():
    global n, m, f
    global space_grid, views, anomalies
    # N, M, F 값 입력 받기
    # N: 미지의 공간 크기 (N x N)
    # M: 시간의 벽 크기 (M x M)
    # F: 시간 이상 현상 개수
    n, m, f = map(int, sys.stdin.readline().split())

    # 미지의 공간 평면도 (N x N) 입력 받기
    # 0: 빈 공간, 1: 장애물, 3: 시간의 벽, 4: 탈출구
    space_grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    # 시간의 벽 단면도 입력 받기
    # views[0]: 동쪽 면, views[1]: 서쪽 면, views[2]: 남쪽 면, views[3]: 북쪽 면, views[4]: 윗면
    # 각 단면도는 M x M 크기
    views = [[list(map(int, sys.stdin.readline().split())) for _ in range(m)] for _ in range(5)]

    # 시간 이상 현상 정보 입력 받기 (r, c, d, v)
    # r, c: 시작 위치, d: 확산 방향 (0:동, 1:서, 2:남, 3:북), v: 확산 주기
    anomalies = [tuple(map(int, sys.stdin.readline().split())) for _ in range(f)]


def find_exit_and_goal(wall_base_r, wall_base_c):
    """
    미지의 공간 평면도에서 시간의 벽과 맞닿은 유일한 출구를 찾고,
    해당 출구가 시간의 벽의 어느 면의 어느 상대 좌표에 해당하는지 매핑합니다.
    """
    plane_exit_r, plane_exit_c = -1, -1  # 미지의 공간 평면도 상의 출구 좌표
    goal_face, goal_r, goal_c = -1, -1, -1  # 시간의 벽 면에서의 상대 좌표

    # 북쪽 출구 탐색: 시간의 벽 위쪽 (wall_base_r - 1) 행
    # 벽이 격자 상단에 붙어있지 않고, 해당 위치가 장애물이나 벽이 아닌 빈 공간(0)일 경우
    if wall_base_r > 0:
        for c_off in range(m):  # 벽의 열 범위 (wall_base_c ~ wall_base_c + m - 1)
            if space_grid[wall_base_r - 1][wall_base_c + c_off] == 0:  # 빈 공간(0)인지 확인
                plane_exit_r, plane_exit_c = wall_base_r - 1, wall_base_c + c_off
                # 북쪽 면에서 출구는 r=m-1 (가장 아래), c는 윗면에서 봤을 때의 c와 반대 방향으로 매핑됨 (m-1-c_off)
                goal_face, goal_r, goal_c = NORTH, m - 1, m - c_off - 1
                break
        if goal_face != -1: return plane_exit_r, plane_exit_c, goal_face, goal_r, goal_c

    # 남쪽 출구 탐색: 시간의 벽 아래쪽 (wall_base_r + m) 행
    if wall_base_r + m < n:
        for c_off in range(m):  # 벽의 열 범위 (wall_base_c ~ wall_base_c + m - 1)
            if space_grid[wall_base_r + m][wall_base_c + c_off] == 0:
                plane_exit_r, plane_exit_c = wall_base_r + m, wall_base_c + c_off
                # 남쪽 면에서 출구는 r=m-1 (가장 아래), c는 벽의 c_off와 동일하게 매핑
                goal_face, goal_r, goal_c = SOUTH, m - 1, c_off
                break
        if goal_face != -1: return plane_exit_r, plane_exit_c, goal_face, goal_r, goal_c

    # 서쪽 출구 탐색: 시간의 벽 왼쪽 (wall_base_c - 1) 열
    if wall_base_c > 0:
        for r_off in range(m):  # 벽의 행 범위 (wall_base_r ~ wall_base_r + m - 1)
            if space_grid[wall_base_r + r_off][wall_base_c - 1] == 0:
                plane_exit_r, plane_exit_c = wall_base_r + r_off, wall_base_c - 1
                # 서쪽 면에서 출구는 r=m-1 (가장 아래), c는 벽의 r_off와 동일하게 매핑
                goal_face, goal_r, goal_c = WEST, m - 1, r_off
                break
        if goal_face != -1: return plane_exit_r, plane_exit_c, goal_face, goal_r, goal_c

    # 동쪽 출구 탐색: 시간의 벽 오른쪽 (wall_base_c + m) 열
    if wall_base_c + m < n:
        for r_off in range(m):  # 벽의 행 범위 (wall_base_r ~ wall_base_r + m - 1)
            if space_grid[wall_base_r + r_off][wall_base_c + m] == 0:
                plane_exit_r, plane_exit_c = wall_base_r + r_off, wall_base_c + m
                # 동쪽 면에서 출구는 r=m-1 (가장 아래), c는 윗면에서 봤을 때의 r과 반대 방향으로 매핑됨 (m-1-r_off)
                goal_face, goal_r, goal_c = EAST, m - 1, m - r_off - 1
                break
        if goal_face != -1: return plane_exit_r, plane_exit_c, goal_face, goal_r, goal_c

    # 모든 방향을 탐색했지만 출구를 찾지 못한 경우
    return plane_exit_r, plane_exit_c, goal_face, goal_r, goal_c


# --- Phase 1: 시간의 벽 표면 탈출 --- #
def calc_escape_time_3d():
    global views

    # 1-1. 시작점과 목표 지점 설정

    # 타임머신 시작 위치 찾기 (윗면에서 2로 표시된 곳)
    start_face, start_r, start_c = -1, -1, -1
    for r in range(m):
        for c in range(m):
            if views[TOP][r][c] == 2:
                start_face, start_r, start_c = TOP, r, c
                views[TOP][r][c] = 0  # 시작점은 이제 빈 공간으로 간주하여 BFS 탐색에 방해되지 않도록 합니다.
                break
        if start_face != -1: break  # 시작점을 찾았으면 루프 종료

    # 미지의 공간 평면도에서 시간의 벽(3)의 좌상단 위치 찾기
    wall_base_r, wall_base_c = -1, -1
    for r in range(n):
        if 3 in space_grid[r]:
            wall_base_r, wall_base_c = r, space_grid[r].index(3)
            break

    # 시간의 벽에서 미지의 공간으로 이어지는 출구 (plane_exit)와
    # 그 출구에 해당하는 시간의 벽 옆면의 상대 좌표 (goal_face, goal_r, goal_c) 찾기
    plane_exit_r, plane_exit_c, goal_face, goal_r, goal_c = find_exit_and_goal(wall_base_r, wall_base_c)

    # 출구를 찾지 못했거나, 찾은 출구가 시간의 벽 단면도 상에서 장애물인 경우 탈출 불가능
    # (find_exit_and_goal에서 0인 곳만 찾지만, 혹시 모를 예외 처리)
    if goal_face == -1 or views[goal_face][goal_r][goal_c] == 1:
        return -1, -1, -1

    # 1-2. 표면 이동 BFS (deque 사용)
    # 큐: (현재 시간, 현재 면, 현재 면 내의 행, 현재 면 내의 열)
    q_surf = deque([(0, start_face, start_r, start_c)])
    # 방문 기록: (면, 행, 열) 튜플을 저장하는 배열. 중복 탐색 방지.
    visited_surf = [
        [
            [False] * m
            for _ in range(m)
        ] for _ in range(5)
    ]
    visited_surf[start_face][start_r][start_c] = True
    time_to_exit_wall = -1  # 시간의 벽을 탈출하는 데 걸리는 시간

    while q_surf:
        time, face, r, c = q_surf.popleft()

        # 목표 지점(시간의 벽 출구)에 도달했으면 시간 기록 후 BFS 종료
        # +1을 하는 이유는, 해당 칸에 도달하는 데 걸린 시간(time)에 1턴을 더하여
        # 다음 턴에 미지의 공간 바닥으로 내려갈 수 있음을 의미합니다.
        if (face, r, c) == (goal_face, goal_r, goal_c):
            time_to_exit_wall = time + 1
            break

        # 1. 같은 면 내에서 이동 (상하좌우 4방향)
        dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]  # 상, 하, 좌, 우
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            # 면 내 유효 범위 확인 (0 <= nr, nc < M)
            if 0 <= nr < m and 0 <= nc < m:
                # 이동할 칸이 빈 공간(0)이고 아직 방문하지 않았다면
                if views[face][nr][nc] == 0 and visited_surf[face][nr][nc] == False:
                    visited_surf[face][nr][nc] = True  # 방문 기록
                    q_surf.append((time + 1, face, nr, nc))  # 큐에 추가 (시간 1 증가)

        # 2. 다른 면으로 이동 (면의 가장자리에서 인접한 면으로)
        transitions = []  # (다음 면, 다음 면 내의 행, 다음 면 내의 열) 튜플 리스트

        # 윗면(TOP)에서 다른 면으로 이동 규칙
        if face == TOP:
            if r == 0:      transitions.append((NORTH, 0, m - c - 1))  # 윗면의 0행(북쪽 가장자리) -> 북쪽 면의 0행 (열은 반전)
            if r == m - 1:  transitions.append((SOUTH, 0, c))  # 윗면의 m-1행(남쪽 가장자리) -> 남쪽 면의 0행 (열은 그대로)
            if c == 0:      transitions.append((WEST, 0, r))  # 윗면의 0열(서쪽 가장자리) -> 서쪽 면의 0행 (행은 그대로)
            if c == m - 1:  transitions.append((EAST, 0, m - r - 1))  # 윗면의 m-1열(동쪽 가장자리) -> 동쪽 면의 0행 (행은 반전)
        # 북쪽 면(NORTH)에서 다른 면으로 이동 규칙
        elif face == NORTH:
            if r == 0:      transitions.append((TOP, 0, m - c - 1))  # 북쪽 면의 0행 -> 윗면의 0행 (열은 반전)
            if c == m - 1:  transitions.append((WEST, r, 0))  # 북쪽 면의 m-1열 -> 서쪽 면의 r행 (0열)
            if c == 0:      transitions.append((EAST, r, m - 1))  # 북쪽 면의 0열 -> 동쪽 면의 r행 (m-1열)
        # 남쪽 면(SOUTH)에서 다른 면으로 이동 규칙
        elif face == SOUTH:
            if r == 0:      transitions.append((TOP, m - 1, c))  # 남쪽 면의 0행 -> 윗면의 m-1행 (열은 그대로)
            if c == 0:      transitions.append((WEST, r, m - 1))  # 남쪽 면의 0열 -> 서쪽 면의 r행 (m-1열)
            if c == m - 1:  transitions.append((EAST, r, 0))  # 남쪽 면의 m-1열 -> 동쪽 면의 r행 (0열)
        # 서쪽 면(WEST)에서 다른 면으로 이동 규칙
        elif face == WEST:
            if r == 0:      transitions.append((TOP, c, 0))  # 서쪽 면의 0행 -> 윗면의 c열 (0행)
            if c == 0:      transitions.append((NORTH, r, m - 1))  # 서쪽 면의 0열 -> 북쪽 면의 r행 (m-1열)
            if c == m - 1:  transitions.append((SOUTH, r, 0))  # 서쪽 면의 m-1열 -> 남쪽 면의 r행 (0열)
        # 동쪽 면(EAST)에서 다른 면으로 이동 규칙
        elif face == EAST:
            if r == 0:      transitions.append((TOP, m - c - 1, m - 1))  # 동쪽 면의 0행 -> 윗면의 m-1열 (행은 반전)
            if c == m - 1:  transitions.append((NORTH, r, 0))  # 동쪽 면의 m-1열 -> 북쪽 면의 r행 (0열)
            if c == 0:      transitions.append((SOUTH, r, m - 1))  # 동쪽 면의 0열 -> 남쪽 면의 r행 (m-1열)

        for next_face, next_r, next_c in transitions:
            # 이동할 칸이 빈 공간(0)이고 아직 방문하지 않았다면
            if views[next_face][next_r][next_c] == 0 and visited_surf[next_face][next_r][next_c] == False:
                visited_surf[next_face][next_r][next_c] = True  # 방문 기록
                q_surf.append((time + 1, next_face, next_r, next_c))  # 큐에 추가 (시간 1 증가)

    # 시간의 벽을 탈출하는데 걸린 시간 반환
    return time_to_exit_wall, plane_exit_r, plane_exit_c


# --- Phase 2: 미지의 공간 횡단 --- #
def calc_dest_time_2d(time_to_exit_wall, plane_exit_r, plane_exit_c):
    # Phase 1에서 탈출에 실패했다면, Phase 2도 불가능
    if time_to_exit_wall == -1:
        return -1

    # 미지의 공간 평면도에서 최종 탈출구(4) 위치 찾기
    escape_r, escape_c = -1, -1
    for r in range(n):
        if 4 in space_grid[r]:
            escape_r, escape_c = r, space_grid[r].index(4)
            break

    # 시간 이상 현상에 의해 각 칸이 언제부터 막히는지 기록하는 배열
    # anomaly_blocks[r][c] = (r,c) 칸이 막히는 가장 빠른 시간
    # 초기값은 무한대로 설정하여, 막히지 않는 칸은 계속 무한대 값을 가집니다.
    anomaly_blocks = [[float('inf')] * n for _ in range(n)]

    # 시간 이상 현상 확산 방향 (동, 서, 남, 북)
    # 문제에서 주어진 방향: 동(0), 서(1), 남(2), 북(3)
    anomaly_dr, anomaly_dc = [0, 0, 1, -1], [1, -1, 0, 0]  # E, W, S, N

    # 각 시간 이상 현상에 대해 확산 경로 및 차단 시간 전처리
    for r_i, c_i, d_i, v_i in anomalies:
        # 시작 위치가 탈출구(4)가 아닌 경우에만 시간 이상 현상으로 막힐 수 있음
        if space_grid[r_i][c_i] != 4:
            anomaly_blocks[r_i][c_i] = min(anomaly_blocks[r_i][c_i], 0)

        time_step, next_r, next_c = v_i, r_i, c_i
        while True:
            next_r, next_c = next_r + anomaly_dr[d_i], next_c + anomaly_dc[d_i]
            # 격자 범위를 벗어나거나, 장애물(1)이거나, 탈출구(4)인 경우 확산 중단
            if not (0 <= next_r < n and 0 <= next_c < n) or space_grid[next_r][next_c] in [1, 4]:
                break
            # 해당 칸이 막히는 가장 빠른 시간을 갱신
            anomaly_blocks[next_r][next_c] = min(anomaly_blocks[next_r][next_c], time_step)
            time_step += v_i  # 다음 확산 시간

    # BFS 큐: (현재 시간, 현재 행, 현재 열)
    # 시작 시간은 시간의 벽을 탈출하는 데 걸린 시간입니다.
    q_2d = deque([(time_to_exit_wall, plane_exit_r, plane_exit_c)])
    # 같은 칸이라도 더 빠른 시간에 도달하는 경로가 있다면 갱신하기 위함입니다.
    # visited_2d[r][c]는 (r,c)에 도달하는 최소 시간을 저장합니다.
    visited_2d = [
        [float('inf')] * n for _ in range(n)
    ]
    visited_2d[plane_exit_r][plane_exit_c] = time_to_exit_wall

    while q_2d:
        time, cr, cc = q_2d.popleft()

        # 최종 탈출구에 도달했으면 현재 시간 반환
        if (cr, cc) == (escape_r, escape_c):
            return time

        # 상하좌우 4방향 이동
        dr, dc = [-1, 1, 0, 0], [0, 0, 1, -1]  # 상, 하, 우, 좌 (문제의 방향과 일치하도록)
        for i in range(4):
            nr, nc = cr + dr[i], cc + dc[i]
            next_time = time + 1  # 다음 칸으로 이동하는 데 걸리는 시간

            # 이동 조건 확인:
            # 1. 격자 범위 내에 있는지
            # 2. 장애물(1)이나 시간의 벽(3)이 아닌지 (시간의 벽은 2D 평면에서 장애물로 간주)
            # 3. 다음 시간에 해당 칸이 시간 이상 현상으로 막히지 않는지 (next_time < anomaly_blocks[nr][nc])
            # 4. 이미 방문했더라도 현재 경로가 더 빠른지 (next_time < visited_2d[nr][nc])
            if (0 <= nr < n and 0 <= nc < n) and \
                    space_grid[nr][nc] not in [1, 3] and \
                    next_time < anomaly_blocks[nr][nc] and \
                    next_time < visited_2d[nr][nc]:
                # 이동 가능하면 방문 기록 갱신 및 큐에 추가
                visited_2d[nr][nc] = next_time
                q_2d.append((next_time, nr, nc))

    # 모든 경로를 탐색했지만 탈출구에 도달하지 못했다면 -1 반환
    return -1


# --- 메인 실행 --- #
if __name__ == '__main__':
    read_input()
    # Phase 1: 시간의 벽 표면 탈출 시간 계산
    time_to_exit_wall, plane_exit_r, plane_exit_c = calc_escape_time_3d()
    # Phase 2: 미지의 공간 횡단 시간 계산
    time_to_goal = calc_dest_time_2d(time_to_exit_wall, plane_exit_r, plane_exit_c)
    print(time_to_goal)
