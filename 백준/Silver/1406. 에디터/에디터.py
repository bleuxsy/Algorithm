import sys
# sentence = list(input())
# cursor = len(sentence)
# N = int(input())
# for i in range(N):
#   command = list(input().split())
#   if command[0] == 'P':
#     sentence.insert(cursor ,command[1])
#     cursor += 1
#   elif command[0] == 'L':
#     if cursor > 0:
#         cursor -= 1
#   elif command[0] == 'D':
#     if cursor > 0:
#       cursor += 1
#   elif command[0] == 'B':
#     if cursor< len(sentence):
#       cursor += 1
#     sentence.remove(sentence[cursor-1])
#stack 으로 표현
stack_left = list(input())
stack_right = []
N = int(input())
for _ in range(N):
  command = sys.stdin.readline().split()

  if command[0] == "L" and stack_left:
    stack_right.append(stack_left.pop())
  elif command[0] == "D" and stack_right:
    stack_left.append(stack_right.pop())
  elif command[0] == "B" and stack_left:
    stack_left.pop()
  elif command[0] == "P":
    stack_left.append(command[1])
print("".join(stack_left + list(reversed(stack_right))))
