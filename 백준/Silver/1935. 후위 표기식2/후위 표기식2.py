N = int(input()) 
word = input()  
num = []  
stack = []


for _ in range(N):
    num.append(int(input()))

for i in word:
    if i in "+-*/":
        a = stack.pop()
        b = stack.pop()
        if i == "+":
            stack.append(b + a)
        elif i == "-":
            stack.append(b - a)
        elif i == "*":
            stack.append(b * a)
        elif i == "/":
            stack.append(b / a)
    else:
       
        stack.append(num[ord(i) - ord("A")])


print("{:.2f}".format(stack[0]))
