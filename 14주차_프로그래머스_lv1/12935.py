def solution(arr):
    answer = []
    minV = min(arr)
    for i in arr:
        if i != minV:
            answer.append(i)
    if answer == []:
        answer= [-1]
            
    return answer
# 제일 작은 수 제거하기