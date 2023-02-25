def solution(t, p):
    answer = 0
    temp = []
    cut = len(p)
    for i in range(len(t)-cut + 1):
        temp.append(int(t[i:i+cut]))
    num = int(p)
    for i in temp:
        if i <= num:
            answer += 1
    return answer
# 아래는 더 짧은 코드로 바꾸기.
def solution(t, p):
    answer = 0
    for i in range(len(t)-len(p) + 1):
        if int(t[i:i+len(p)]) <= int(p):
            answer += 1
    return answer
# 크기가 작은 부분 문자열