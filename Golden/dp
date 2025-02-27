a ,b,c = map(int,input().split())
if a < 11 : 
    print(-1)
elif a == 11 and b < 11:
    print(-1)
else:
    num =(a*24*60+b*60+c) -(11*24*60+11*60+11)
    print(num)

n = int(input())
arr = list(map(int,input().split()))
for i in range(1,n):
    for j in range(0,i):
        if arr[i] < arr[j]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
for k in arr:
    print(k, end=" ")