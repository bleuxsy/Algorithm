import sys
N = int(input())
info = []
for i in range(N):
  age, name = input().split()
  info.append([int(age), name])
info.sort(key =lambda x :int(x[0])) #람다는 함수를 쉽게 정의
for age, name in info:
  print(age, name)
