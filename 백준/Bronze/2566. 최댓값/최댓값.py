max_key = 0
max_col = 0
# for i in range(9):
#   mylist = [list(map(int, input().split()))]
#   col = mylist.index(max(mylist))
#   key = max(mylist)
#   row = i
#   if max_key < key :
#     max_key = key
#     max_col = col
#     max_row = i
mylist = [list(map(int, input().split())) for _ in range(9)]
for row in range(9):
  for col in range(9):
    if max_key <= mylist[row][col]:
      max_row = row+1
      max_col = col+1
      max_key = mylist[row][col]
print(max_key)
print(max_row, max_col)

  