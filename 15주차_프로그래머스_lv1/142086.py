def solution(s):
    answer = []
    temp = dict()
    for i in range(len(s)):
        if s[i] not in temp:
            answer.append(-1)
        else:
            answer.append(i-temp[s[i]])
        temp[s[i]] = i
    return answer
# 가장 가까운 글자. 딕셔너리 이용.