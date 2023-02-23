def solution(d, budget):
    answer = 0
    d.sort()
    for i in d:
        temp = budget - i
        if temp >= 0:
            answer += 1
            budget = temp
        else:
            break
    return answer