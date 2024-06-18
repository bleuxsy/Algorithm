mylist = [input() for _ in range(5)]
for i in range(15):
  for j in range(5):
    if i < len(mylist[j]):
      print(mylist[j][i], end = '') #줄바꿈을 하지 않고 출력
