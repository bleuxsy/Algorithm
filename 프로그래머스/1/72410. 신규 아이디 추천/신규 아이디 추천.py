import copy
def check(new_id):
    # 1단계: 소문자 치환
    new_id = new_id.lower()
    
    # 2단계: 허용 문자만 남기기
    allowed = "abcdefghijklmnopqrstuvwxyz0123456789-_."
    new_id = "".join([ch for ch in new_id if ch in allowed])
    
    # 3단계: 마침표 연속 → 하나로
    while ".." in new_id:
        new_id = new_id.replace("..", ".")
    
    # 4단계: 처음/끝 마침표 제거
    new_id = new_id.strip(".")
    
    # 5단계: 빈 문자열이면 "a"
    if not new_id:
        new_id = "a"
    
    # 6단계: 16자 이상이면 앞 15자만, 끝이 '.'이면 제거
    new_id = new_id[:15].rstrip(".")
    
    # 7단계: 길이가 2 이하라면 마지막 문자를 길이 3 될 때까지 반복
    while len(new_id) < 3:
        new_id += new_id[-1]
    
    return new_id
def solution(new_id):
    answer = ''
    
    
    return check(new_id)