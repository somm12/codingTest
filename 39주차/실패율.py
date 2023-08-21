def solution(n,stages):
    answer = [[]]

    arr = [0]*(n+2)
    passUser = len(stages)# 지금 스테이지까지 도달한 사용자 수(도전자 포함.)
    for v in stages:
        arr[v] += 1
    for i in range(1,n+1):
        if passUser > 0:
            rate = arr[i]/passUser # 0이 분모가 될 수 있음에 유의
        else:
            rate=0
        answer.append([i,rate])
        passUser -= arr[i]
    answer = answer[1:]
    answer.sort(key=lambda x:(-x[1],x[0]))


    return [v[0] for v in answer]
# 아직 아무도 도달하지 않은 스테이지라면 실패율은 0.
# 프로그래머스 실패율.