def solution(users, emoticons):
    discount = []
    answer = [0] * 2
    sales = [10, 20, 30 , 40]
    def dfs(L, temp):
        if L == len(emoticons):
            discount.append(temp[:])
            return 
        for s in sales:
            temp[L] += s
            dfs(L+1, temp)
            temp[L] -= s
    dfs(0 , [0] * len(emoticons))

    
    for d in range(len(discount)):
        plus_user = 0 
        profit = 0
        
        for user in users:
            emoticon_buy = 0
            for i in range(len(emoticons)):
                if discount[d][i] >= user[0]:
                    emoticon_buy += emoticons[i] * ((100 - discount[d][i]) / 100)
            if user[1] <= emoticon_buy:
                plus_user += 1
            else:
                profit += emoticon_buy
        if answer[0] < plus_user:
            answer = [plus_user , int(profit)]
        elif answer[0] == plus_user:
            if answer[1] < profit:
                answer = [plus_user, int(profit)]
    
    print(answer)
    return answer