def solution(n, lost, reserve):
    answer = n - len(lost)
    lost.sort()
    reserve.sort()
    new_lost = [i for i in lost if not i in reserve]
    new_reserve = [i for i in reserve if not i in lost]
    answer += len(lost) - len(new_lost)
                
    for i in new_lost:
        if i-1 in new_reserve:
            answer += 1
            new_reserve.remove(i-1 )
        elif i+1 in new_reserve:
            answer += 1
            new_reserve.remove(i+1)
    
    return answer
# 체육복