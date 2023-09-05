from bisect import bisect_left
def solution(info,query):
    answer = []
    dict = {}
    # 나올 수 있는 경우를 나타낸 배열. 4*27 가지 존재.
    arr = [['cpp','java','python','-'],['backend','frontend','-'],['junior','senior','-'],['chicken','pizza','-']]
    def dfs(res,L):
        if L == 4:# 한 경우가 만들어졌다면, dict에 넣기.
            res = tuple(res)
            dict[res] = []
            return
        for v in arr[L]:
            dfs(res+[v],L+1)
    dfs([],0)
  
    for s in info:# 현재 info가 dict에 해당하는 모든 경우에 속한다면 ex) java, be, junior, pizza >= - - junion pizza.
        a,b,c,d,score = s.split()
        score = int(score)
        for condition in dict:
            tmp = ' '.join(condition)
            tmp = tmp.replace('-','')# -를 먼저 없애고,
            tmp = tmp.split()# 다시 split한 다음. 집합으로 만들고 포함되는지 확인.
            if set([a,b,c,d]) >= set(tmp):
                dict[condition].append(score)# 해당 경우에 속하는 모든 점수를 append
   
    for condition in dict:
        dict[condition].sort()# 정렬을 해서 몇 점이상 점수가 몇 개인지 쉽게 알아내보기.
    
    for v in query:# 이분탐색을 이용해서 몇 명인지 알아내기
        a,b,c,d = v.split(" and ")
        d, score = d.split()
        score = int(score)
        idx = bisect_left(dict[(a,b,c,d)],score)# 몇 점이상 중 가장 왼쪽 인덱스 구하기
        answer.append(len(dict[(a,b,c,d)])-idx) # len-idx => 몇 개인지 나타냄.
            
    return answer