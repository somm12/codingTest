
from collections import Counter
def combi(n,all):# all 배열 원소 중에서 n개 조합 만들기.
    ans = []
    def comb(res,start):
        if len(res) == n:
            res = list(res)
            res.sort()
            ans.append(''.join(res))
            return
        for i in range(start,len(all)):
            comb(res+all[i],i+1)
    comb('',0)
    return ans
def solution(orders,course):
    answer = []

    for cnt in course:
        cand = []# cnt 개수 만큼의 가장 많이 함께 주문된 코스요리 조합을 담을 배열.
        
        for order in orders:
            arr = combi(cnt,list(order))
            for v in arr:
                cand.append(v)
                
        order_count = Counter(cand).most_common()# 가장 많이 주문된 조합 먼저 순서대로 반환.
        if order_count and order_count[0][1] > 1:# 2개이상인지 확인.
            maxV = order_count[0][1]
            for v,cnt in order_count:# 가장 많은 개수가 여러개라면 모두 answer에 추가.
                if cnt == maxV:
                    answer.append(v)
            
    answer.sort()
    return answer
# 프로그래머스 문제