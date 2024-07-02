N  = int(input())
mynum = list(map(str,input().split()))
M = int(input())
yournum = list(map(str,input().split()))
result ={}
for i in yournum:
  result[i] = 0
for j in mynum:
  if j in result:
    result[j] = 1
for i in result:
  print(result[i], end=" ")
