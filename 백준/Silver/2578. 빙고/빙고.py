def check_row():
    count = 0
    for row in board:
        if sum(row) == 5:
            count += 1
    return count

def check_col():
    count = 0
    for col in range(5):
        col_sum = 0
        for row in range(5):
            col_sum += board[row][col]
        if col_sum == 5:
            count += 1
    return count

def check_dia():
    count = 0
    if sum([board[i][i] for i in range(5)]) == 5:
        count += 1
    if sum([board[i][4-i] for i in range(5)]) == 5:
        count += 1
    return count

def bingo(s):
    for k in range(5):
        for l in range(5):
            if mylist[k][l] == s:
                board[k][l] = 1
                return  

mylist = [list(map(int, input().split())) for _ in range(5)]
your_list = [list(map(int, input().split())) for _ in range(5)]
board = [[0]*5 for _ in range(5)]

ccnt = 0
for i in range(5):
    for j in range(5):
        ccnt += 1
        bingo(your_list[i][j])
        total = check_row() + check_col() + check_dia()
        if total >= 3:
            print(ccnt)
            exit()