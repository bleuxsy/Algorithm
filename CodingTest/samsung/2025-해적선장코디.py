import sys, heapq
sys.stdin = open("input.txt", "r")

def move_ready():
    while cool_heap and cool_heap[0][0] <= time:
        available_time, boat_id = heapq.heappop(cool_heap)


        if status.get(boat_id) == ("cool", available_time):
            status[boat_id] = "ready"
            p, r = boat[boat_id]
            heapq.heappush(ready_heap, (-p, boat_id))

def fight():
    move_ready()

    total_p = 0
    picked = []

    while ready_heap and len(picked) < 5:
        neg_p, boat_id = heapq.heappop(ready_heap)

        # 이미 ready가 아니면 버림
        if status.get(boat_id) != "ready":
            continue

        cur_p, cur_r = boat[boat_id]

        # 예전 공격력 정보면 버림
        if -neg_p != cur_p:
            continue

        total_p += cur_p
        picked.append(boat_id)

        # 지금부터 재장전
        available_time = time + cur_r
        status[boat_id] = ("cool", available_time)
        heapq.heappush(cool_heap, (available_time, boat_id))

    print(total_p, len(picked), *picked)


T = int(input())

boat = {}       # boat[id] = (p, r)
status = {}     # "ready" or ("cool", available_time)
ready_heap = [] # (-p, id)
cool_heap = []  # (available_time, id)

time = 0

for _ in range(T):
    data = list(map(int, input().split()))
    cmd = data[0]

    move_ready()

    if cmd == 100:
        N = data[1]

        boat.clear()
        status.clear()
        ready_heap.clear()
        cool_heap.clear()

        idx = 2
        for _ in range(N):
            boat_id = data[idx]
            p = data[idx + 1]
            r = data[idx + 2]
            idx += 3

            boat[boat_id] = (p, r)
            status[boat_id] = "ready"
            heapq.heappush(ready_heap, (-p, boat_id))

    elif cmd == 200:
        boat_id, p, r = data[1], data[2], data[3]
        boat[boat_id] = (p, r)
        status[boat_id] = "ready"
        heapq.heappush(ready_heap, (-p, boat_id))

    elif cmd == 300:
        boat_id, new_p = data[1], data[2]
        old_p, old_r = boat[boat_id]
        boat[boat_id] = (new_p, old_r)


        if status[boat_id] == "ready":
            heapq.heappush(ready_heap, (-new_p, boat_id))

    elif cmd == 400:
        fight()

    time += 1