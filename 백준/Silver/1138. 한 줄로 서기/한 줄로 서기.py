N = int(input())
person = list(map(int,input().split()))
array = [0] * N
for h in range(1, N+1):
    cnt = 0
    for i in range(N):
        if array[i] == 0:
            if cnt == person[h-1]:
                array[i] = h
                break
            cnt += 1

print(*array)

