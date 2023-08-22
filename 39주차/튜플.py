def solution(s):
    answer =[]
    arr= []
    s = s[2:-2]
    
    for a in s.split("},{"):
        tmp = list(map(int,a.split(",")))# 문자열을 각 배열로 만들어서 추가.
        arr.append(tmp)
    
    
    arr.sort(key=lambda x:len(x))# 배열 원소개수 작은것 부터 정렬.

    res = {}
    for r in arr:# 하나씩 값을 추가한다.
        for v in r:
            if v not in answer:
                res[v] = 1
    for key in res.keys():
        answer.append(key)
             
            
    return answer
# 프로그래머스 카카오인턴 문제