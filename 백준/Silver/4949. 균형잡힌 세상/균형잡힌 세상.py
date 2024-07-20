while(True):
  word = input()
  stack = []
  if word ==".":
    break
  for data in word: 
    if data =='[' or data =='(':
      stack.append(data)
    elif data ==']':
      if len(stack)!= 0 and stack[-1] == '[':
        stack.pop()
      else : 
        stack.append(']')
        break
    elif data == ')':
      if len(stack) != 0 and stack[-1] =='(':
        stack.pop()
      else:
        stack.append(')')
        break
  if len(stack) == 0 :
      print("yes")
  else:
      print("no")