t = int(input())
A = list(map(int, input().split()))
B= sorted(A)
res = B[0] * B[t-1]
print(res)



