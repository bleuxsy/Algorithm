# 문제 7 
from collections import deque

def is_valid_move(x, y):
    return -5 <= x <= 5 and -5 <= y <= 5

def solutions(x, y, dirs):
    visited = set()
    current_x, current_y = x, y
    
    for dir in dirs:
        next_x, next_y = current_x, current_y
        
        if dir == 'U':
            next_y += 1
        elif dir == 'D':
            next_y -= 1
        elif dir == 'L':
            next_x -= 1
        elif dir == 'R':
            next_x += 1
        
        if not is_valid_move(next_x, next_y):
            continue
        
        path = ((current_x, current_y), (next_x, next_y))
        reverse_path = ((next_x, next_y), (current_x, current_y))
        
        if path not in visited and reverse_path not in visited:
            visited.add(path)
            visited.add(reverse_path)
        
        current_x, current_y = next_x, next_y
    
    return len(visited) // 2

# 예제 실행
print(solutions(0, 0, "ULURRDLLU")) 
print(solutions(0, 0, "LLLLLLLUU"))  
