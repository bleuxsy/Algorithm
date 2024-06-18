mylist = list(map(int, input().split()))
if mylist == sorted(mylist) :
  print("ascending")
elif mylist == sorted(mylist, reverse=True):
  print("descending")
else:
  print("mixed")