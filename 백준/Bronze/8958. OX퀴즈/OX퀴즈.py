N = int(input())
for _ in range(N):
  ox = input()
  score = 0
  sum = 0
  for i in ox:
    if(i == 'O'):
      score += 1
    else:
      score = 0
    sum += score
  print(sum)