def timecal(start,end):
    time = 0
    h_a , m_a = map(int, start.split(":"))
    h_b , m_b = map(int, end.split(":"))
    if m_b < m_a :
        h_b -= 1
        m_b += 60
    time += (h_b - h_a) *60
    time += (m_b - m_a)
    print(time)
    return time
def feecal(times , m , f , pm , pf):
    if times > m and (times-m) % pm == 0:
        return f + (times-m)/pm * pf
    if times <= m:
        return f
    else:
        return f + ((times-m)//pm +1) * pf
def solution(fees, records):
    answer = []
    dic = {}
    
    total = []
    
    for record in records:
        a,b,c = record.split()
        if b not in dic:
            dic[b] = []
        dic[b].append([a,c])
    
    
    sorted_items = sorted(dic.items())
    diC = dict(sorted_items)
    print(diC)
    minute = fees[0]
    fee = fees[1]
    per_minute = fees[2]
    per_fee = fees[3]
    for num in diC:
        times = 0
        if len(diC[num])%2 == 0:
            for i in range(0, len(diC[num])-1 , 2):
                times += timecal(diC[num][i][0] , diC[num][i+1][0])
        else:
            for i in range(0, len(diC[num])-1, 2):
                times += timecal(diC[num][i][0], diC[num][i+1][0])
            times+= timecal(diC[num][len(diC[num])-1][0], "23:59")
        answer.append(feecal(times, minute,fee,per_minute, per_fee)) 
            
    print(times)
    return answer