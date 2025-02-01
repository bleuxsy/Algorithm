S = input()  # 수식 입력받기
stack = []  # 연산자를 저장할 스택
result = ''  # 후위 표기법 결과를 저장할 문자열

for char in S:
    if char.isalpha():  # 알파벳인 경우 
        result += char
    elif char == "(":  # 여는 괄호인 경우
        stack.append(char)
    elif char in '*/':  # 곱셈 또는 나눗셈인 경우
        while stack and stack[-1] in '*/':  # 스택의 상단이 곱셈 또는 나눗셈인 동안
            result += stack.pop()  # 스택에서 꺼내서 결과에 추가
        stack.append(char)  # 현재 연산자를 스택에 추가
    elif char in '+-':  # 덧셈 또는 뺄셈인 경우
        while stack and stack[-1] != '(':  # 스택의 상단이 여는 괄호가 아닌 동안
            result += stack.pop()  # 스택에서 꺼내서 결과에 추가
        stack.append(char)  # 현재 연산자를 스택에 추가
    elif char == ")":  # 닫는 괄호인 경우
        while stack and stack[-1] != '(':  # 스택의 상단이 여는 괄호가 아닌 동안
            result += stack.pop()  # 스택에서 꺼내서 결과에 추가
        stack.pop()  # 여는 괄호 제거

while stack:  # 스택에 남아있는 모든 연산자 처리
    result += stack.pop()

print(result)  # 후위 표기법으로 변환된 결과 출력
