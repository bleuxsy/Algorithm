N = int(input())
mylist = list(map(str,input().split()))
M = int(input())
getcard = list(map(str,input().split()))
result = {}
for i in mylist:
  if i in result:
    result[i]+=1
  else:
    result[i]=1
for j in getcard:
  if j in result:
    print(result[j], end=" ")
  else:
    print('0', end=" ")