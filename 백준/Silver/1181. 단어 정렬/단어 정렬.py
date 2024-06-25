N = int(input())
myword = [str(input()) for _ in range(N)]
myword = list(set(myword))
myword.sort()
myword.sort(key=len)
for i in myword:
  print(i)