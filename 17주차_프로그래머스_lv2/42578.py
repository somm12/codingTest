def solution(clothes):
    answer = 1
    dict = {}
    for i in clothes:
        if i[1] in dict:
            dict[i[1]] += 1
        else:
            dict[i[1]] = 1
    for v in dict.values():
        answer *= (v+1)
    return answer -1
# 위장
# 해시 이용하기.