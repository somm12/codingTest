def solution(progresses, speeds):
    answer = []
    tmp =[]
    q = []
    for i,v in enumerate(progresses):
        a = (100-v) / speeds[i]
        if a == int(a):
            q.append(a)
        else:
            q.append(int(a)+1)
    while q:
        x = q.pop(0)
        tmp.append(x)
        cnt = 1
        while q:
            if tmp[0] >= q[0]:
                q.pop(0)
                cnt += 1
            else:
                tmp.pop()
                break
        answer.append(cnt)
        
    return answer