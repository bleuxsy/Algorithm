data = input()
check = False
stack=[]
ans = ''
for d in data:
	if d == "<":
		check = True
		for i in range(len(stack)):
			ans += stack.pop()
	stack.append(d)
	
	if d ==">":
		check = False
		for i in range(len(stack)):
			ans += stack.pop(0)
	if d ==' ' and check == False: 
		for j in range(len(stack)):
			if j == 0:
				stack.pop()
				continue
			ans += stack.pop()
		ans +=' '
if stack:
	for i in range(len(stack)):
		ans += stack.pop()
		
print(ans)
	
