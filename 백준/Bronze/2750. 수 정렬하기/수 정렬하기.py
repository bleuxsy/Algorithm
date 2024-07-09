N = int(input())
mylist = []
for i in range(N):
  mylist.append(int(input()))
mylist = sorted(mylist)
for i in mylist:
  print(i)