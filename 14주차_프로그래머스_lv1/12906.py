def solution(arr):
    answer = []
    prev = -1
    for i in arr:
        if prev != i:
            answer.append(i)
            prev = i
    return answer
# 같은 숫자는 싫어