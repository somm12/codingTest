def calc(res,users,emoticons):# 이모티콘들의 할인비율이 정해진 후, 서비스 가입자 수와 판매한 금액 구하기
    n = len(users)
    m = len(emoticons)
    service = 0
    getMoney = 0
    for i in range(n):
        purchase = 0
        discount,limit = users[i] # 현재 유저의 할인율 기준과, 구매금액 제한.
        
        discount /= 100 
        for j in range(m):
            if res[j] >= discount: # 기준이상이면 모두 구매.
                purchase += (emoticons[j] - (res[j]*emoticons[j]))
        if purchase >= limit:# 구매금액이 제한금액 이상이라면 서비스 강깁.
            service += 1
        else:
            getMoney += purchase
    return [service, int(getMoney)]     # 소수점 빼서 반환.            
        
def solution(users, emoticons):
    cand = []
    
    n = len(users)
    m = len(emoticons)
    discount = [0.1,0.2,0.3,0.4] # 10~ 40% 사이.
    def dfs(res):# 중복 순열 만들기.( 이모티콘 각 할인율 정하기 )
        if len(res) == m:
            v = calc(res,users,emoticons)# 할인율 적용해서 서비스 가입자수, 판매금액 구하기.

            cand.append(v)# 후보 배열에 추가.[(서비스 가입자수, 판매금액)]
            return
        for v in discount:
            dfs(res+[v])
    dfs([])    
       
    cand.sort(key=lambda x:(-x[0],-x[1]))# 목적은 가입자수 많고 > 판매금액 많이 순으로 정렬.
 
    return cand[0]
# 프로그래머스 문제