N = int(input())
#딕셔너리 사용
myword = {}
for i in range(N):
  word = input()
  if word not in myword:
    myword[word] = 1
  else:
    myword[word] += 1
max = max(myword.values())
result=[]
for k,v in myword.items():
  if v == max:
    result.append(k)
result.sort()
print(result[0])