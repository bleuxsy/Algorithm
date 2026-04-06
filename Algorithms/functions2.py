import sys

sys.stdin = open("input.txt", "r")


def rebuild_grid():
    global grid
    grid = [[0] * N for _ in range(N)]

    for k in boxes:
        if boxes[k] is None:
            continue

        h, w, x, y = boxes[k]
        for row in range(x, x - h, -1):
            for col in range(y, y + w):
                grid[row][col] = k


def insert_box(k, h, w, c):
    bottom = h - 1

    while True:
        if bottom + 1 >= N:
            break

        can_down = True
        for col in range(c, c + w):
            if grid[bottom + 1][col] != 0:
                can_down = False
                break

        if not can_down:
            break

        bottom += 1

    boxes[k] = (h, w, bottom, c)
    rebuild_grid()


def can_down_one(box_num):
    if boxes[box_num] is None:
        return False

    h, w, x, y = boxes[box_num]

    if x + 1 >= N:
        return False

    for col in range(y, y + w):
        below = grid[x + 1][col]
        if below != 0 and below != box_num:
            return False

    return True


def apply_gravity():
    while True:
        moved = False

        order = []
        for k in boxes:
            if boxes[k] is not None:
                h, w, x, y = boxes[k]
                order.append((x, k))

        order.sort(reverse=True)

        for _, box_num in order:
            while can_down_one(box_num):
                h, w, x, y = boxes[box_num]
                boxes[box_num] = (h, w, x + 1, y)
                rebuild_grid()
                moved = True

        if not moved:
            break


def can_move_left(box_num):
    if box_num not in boxes or boxes[box_num] is None:
        return False

    h, w, x, y = boxes[box_num]

    for row in range(x, x - h, -1):
        for col in range(0, y):
            if grid[row][col] != 0:
                return False

    return True


def can_move_right(box_num):
    if box_num not in boxes or boxes[box_num] is None:
        return False

    h, w, x, y = boxes[box_num]
    right_end = y + w - 1

    for row in range(x, x - h, -1):
        for col in range(right_end + 1, N):
            if grid[row][col] != 0:
                return False

    return True


def pop_left():
    visible = []
    seen = set()

    for row in range(N):
        for col in range(N):
            if grid[row][col] != 0:
                box_num = grid[row][col]
                if box_num not in seen:
                    seen.add(box_num)
                    visible.append(box_num)
                break
    visible.sort()
    for box_num in visible:
        if can_move_left(box_num):
            answer.append(box_num)
            boxes[box_num] = None
            rebuild_grid()
            apply_gravity()
            rebuild_grid()
            return box_num

    return -1


def pop_right():
    visible = []
    seen = set()

    for row in range(N):
        for col in range(N - 1, -1, -1):
            if grid[row][col] != 0:
                box_num = grid[row][col]
                if box_num not in seen:
                    seen.add(box_num)
                    visible.append(box_num)
                break

    visible.sort()
    for box_num in visible:
        if can_move_right(box_num):
            answer.append(box_num)
            boxes[box_num] = None
            rebuild_grid()
            apply_gravity()
            rebuild_grid()
            return box_num

    return -1


def remaining_box_count():
    cnt = 0
    for k in boxes:
        if boxes[k] is not None:
            cnt += 1
    return cnt


if __name__ == "__main__":
    N, M = map(int, input().split())

    grid = [[0] * N for _ in range(N)]
    boxes = {}
    answer = []

    for _ in range(M):
        K, H, W, C = map(int, input().split())
        insert_box(K, H, W, C - 1)

    turn_left = True

    while remaining_box_count() > 0:
        if turn_left:
            result = pop_left()
        else:
            result = pop_right()

        if result == -1:
            if turn_left:
                result = pop_right()
            else:
                result = pop_left()

            if result == -1:
                break

        turn_left = not turn_left

    for a in answer:
        print(a)