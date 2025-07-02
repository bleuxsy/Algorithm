def check(board, n):
    max_count = 1
    for i in range(n):
        # 가로 체크
        count = 1
        for j in range(1, n):
            if board[i][j] == board[i][j - 1]:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 1

        # 세로 체크
        count = 1
        for j in range(1, n):
            if board[j][i] == board[j - 1][i]:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 1
    return max_count


n = int(input())
board = [list(input()) for _ in range(n)]

answer = 0

for i in range(n):
    for j in range(n):
        
        if j + 1 < n:
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
            answer = max(answer, check(board, n))
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]  # 원복

        
        if i + 1 < n:
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
            answer = max(answer, check(board, n))
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]  # 원복

print(answer)