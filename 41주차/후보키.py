def check(res,relation):# 유일성 확인 함수. res=> 속성들의 인덱스 조합을 담은 배열.
    n = len(relation)
    for i in range(n):
        now = []
        for j in res:# res를 가지고 해당 속성 배열 만들기.
            now.append(relation[i][j])
        for idx in range(i+1,n):# 나머지 모든 row들과 값이 중복 되는 건 없는지 체크.
            tmp = []
            for j in res:
                tmp.append(relation[idx][j])
            if tmp == now:# 유일성 만족 못함.
                return False
    return True
    
def solution(relation):

    cand = [] # 후보키가 되는 조합을 담을 배열.
    n = len(relation)# row 크기
    m = len(relation[0])# column 크기
    def combi(res,start,total): # total 개수 만큼 조합 구하는 함수.
        if len(res) == total:
            if check(res,relation):# 유일성 확인
                for v in cand: # 최소성 확인. 이미 유일성을 가진 조합을 포함한다면, 후보키가 아님.
                    if set(v) <= set(res):
                        break
                else:
                    cand.append(res)
            return
        for i in range(start,m):
            combi(res+[i],i+1,total)
                    
    for x in range(1,m+1):# 1개 ~ m개 까지의 조합 구하기
        combi([],0,x)
 
    return len(cand)
# 프로그래머스 문제