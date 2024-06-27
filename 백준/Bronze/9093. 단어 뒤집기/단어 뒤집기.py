T = int(input())
for _ in range(T):
  onelist =list(input().split())
  mylist = []
  for word in onelist:
    print(word[::-1], end=' ')

