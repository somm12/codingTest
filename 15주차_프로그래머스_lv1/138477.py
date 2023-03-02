def solution(k, score):
    answer = []
    top = []
    minV = score[0]
    for i in range(min(len(score),k)):
        top.append(score[i])
        if score[i] < minV:
            minV = score[i]
        answer.append(minV)
    if k < len(score): 
        for i in range(k,len(score)):
            if score[i] > minV:
                top.remove(minV)
                top.append(score[i])
                minV = min(top)
                answer.append(minV)
            else:
                answer.append(minV)
    return answer

# 명예의 전당.