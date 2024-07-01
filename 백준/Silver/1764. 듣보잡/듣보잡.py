N , M = map(int, input().split())
#많은 양의 데이터를 볼때는 list 보단 set
myN = set()
myM = set()
NM = []
count =0 
for _ in range(N):
  myN.add(input())
for _ in range(M):
  myM.add(input())
  
# for item in myN:
#   if item in myM:
#     NM.append(item)
#     count+=1
result = sorted(list(myM & myN))
print(len(result))
for i in result:
  print(i)