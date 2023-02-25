def solution(strings, n):
    answer = []
    temp = []
    for i in range(len(strings)):
        temp.append((strings[i][n], strings[i]))
    temp.sort()
    for s in temp:
        answer.append(s[1])
    return answer
# 문자열 내 마음대로 정렬하기