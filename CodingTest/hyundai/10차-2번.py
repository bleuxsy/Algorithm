

def normalize(cells):
    cells = list(cells)
    min_x = min(x for x, y in cells)
    min_y = min(y for x, y in cells)

    norm = sorted((x - min_x, y - min_y) for x, y in cells)
    return tuple(norm)
    # set에 list(가변)는 못 넣고 tuple(불변)은 넣을 수 있음

def dfs(cells, front):

    if len(cells) == 5:
        shapes.add(normalize(cells))
        return

    for x, y in list(front):
        new_cells = set(cells)
        new_cells.add((x,y))

        new_front = set(front)
        new_front.remove((x, y))

        for dx, dy in dirs:
            nx , ny = x + dx , y + dy
            if (nx , ny) not in new_cells:
                new_front.add((nx, ny))

        dfs(new_cells, new_front)
    return



dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
shapes = set()
start = (0, 0)
init_front = set()

for dx, dy in dirs:
    init_front.add((start[0]+dx, start[1]+dy))

dfs({start}, init_front)

placements = []
answer = - 10 **18

for shape in shapes:
    for i in range(N):
        for j in range(M):
            cells = []
            total = 0
            ok = True

            for dx , dy in shape:
                nx , ny  = i + dx, j + dy
                if not (0 <= nx < N and 0 <= ny < M):
                    ok = False
                    break
                cells.append((nx, ny))
                total += grid[nx][ny]
            if ok:
                placements.append((set(cells), total ))

for i in range(len(placements)):
    set1, score1 = placements[i]
    for j in range(i+1, len(placements)):
        set2, score2 = placements[j]

        if len(set1 & set2) == 2:
            answer = max(answer, score1 + score2)


print(answer)