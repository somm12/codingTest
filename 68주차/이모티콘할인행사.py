def solution(users, emoticons):
    answer = []
    m = len(emoticons)
    discount = []
    def dfs(res):
        if len(res) == m:
            discount.append(res)
            return
        for v in [0.1,0.2,0.3,0.4]:
            dfs(res+[v])
    dfs([])
    for rate in discount:
        joined = 0
        earn = 0
        for value,limit in users:
            total = 0
            value /= 100
            for i in range(m):
                if rate[i] >= value:
                    total += (emoticons[i] - (emoticons[i]*rate[i]))# 할인 했을 때 구매 금액.
            if total >= limit:# 구매 금액 기준이상이 되버리면, 서비스 가입.
                joined += 1
            else:# 구매 금액 기준 미만이면, 구매.
                earn += total
        
        answer.append((joined,earn))
    answer.sort(key = lambda x:(-x[0],-x[1]))# 서비스 가입자수 , 판매 금액 큰 순 기준.
    count, money = answer[0]
    return [count,int(money)]