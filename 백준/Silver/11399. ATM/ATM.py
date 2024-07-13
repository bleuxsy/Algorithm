N = int(input())
mylist = list(map(int,input().split()))
mylist.sort()
result = 0
for i in range(1, N+1):
  result += sum(mylist[0:i])
print(result)