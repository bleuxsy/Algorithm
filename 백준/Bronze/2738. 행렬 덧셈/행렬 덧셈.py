N,M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]
result = [[0 for j in range(M) for i in range(N)]]
for i in range(N):
    for j in range(M):
        result = A[i][j] + B[i][j]
        print(result,end=' ')
    print()
        