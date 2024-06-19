while True:
  abc = list(map(int,input().split()))
  if abc[0] == 0 and abc[1] == 0 and abc[2]== 0:
    break
  abc.sort()
  if abc[2]**2 == abc[0]**2 + abc[1]**2:
    print("right")
  else:
    print("wrong")
