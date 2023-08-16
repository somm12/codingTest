from collections import defaultdict
def check(info):
    dict = defaultdict(list)
    for x,y,a in info:
        dict[(x,y)].append(a)
    for x,y,a in info:
        if a == 0:# 기둥
            if y == 0 or (1 in dict[(x-1,y)]) or(1 in dict[(x,y)]) or (0 in dict[(x,y-1)]):
                continue
            else:
                return False
        else:# 보
            if 0 in dict[(x,y-1)] or 0 in dict[(x+1,y-1)] or (1 in dict[(x-1,y)] and 1 in dict[(x+1,y)]):
                continue
            else:
                return False
    return True
def solution(n, build_frame):
    answer = []
    
    for x,y,a,b in build_frame:
        if b == 0:# 삭제
            
            answer = [[i,j,v] for i,j,v in answer if [i,j,v] != [x,y,a]]
            if check(answer):
                continue
            else:
                answer.append([x,y,a])
        else: #설치
            answer.append([x,y,a])
            if check(answer):
                continue
            else:
                answer = [[i,j,v] for i,j,v in answer if [i,j,v] != [x,y,a]]
    
    answer.sort()
    return answer
# 프로그래머스 lv3문제