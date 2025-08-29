def dayss(date, m):
    year, month , day = map(int, date.split(".")) 
    month +=  m
    day -= 1
    if month > 12:
        year += (month-1) //12
        month = (month -1)%12 +1
    if day < 1: 
        month-=1
        day += 28
        if month < 1: 
            year -= (month-1) //12
            month += (month -1)%12 +1
            
    print(str(year)+"."+str(month)+"."+str(day))
    return year * 10000 + month * 100 + day
def solution(today, terms, privacies):
    answer = []
    date = ""
    kind = ""
    term  = {}
    for i in range(len(terms)):
        a , b = terms[i].split(" ")
        term[a]= []
        term[a] = int(b) 
    for j in range(len(privacies)):
        date , kind = privacies[j].split(" ")
        print(term[kind])
        y, m , d = map(int, today.split("."))
        todays = y*10000 + m*100 + d
        if todays > dayss(date , term[kind]):
            answer.append(j+1)
        
    print(term)
    return answer