T = int(input())
mylist =[[0] *100 for _ in range(100)]
for i in range(T):
  y, x = map(int,input().split())

  for i in range(x, x+10):
    for j in range(y , y+10):
      mylist[i][j] = 1
result = 0
for i in range(100):
  result += mylist[i].count(1)
print(result)
