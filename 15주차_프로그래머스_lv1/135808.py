def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    for i in range(0,len(score),m):
        if i+m <= len(score):
            minV = min(score[i:i+m])
            answer += minV*m
    return answer
#과일장수. 
# 생각해보면 정렬을 했기 때문에 m의 배수 번째마다 각 상자의 최소 점수를 의미한다!
# 따라서 아래와 같이 더 간단히 구현 가능.

def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    for i in range(0,len(score),m):
        if i+m <= len(score):
            answer += (score[i+m-1])*m
    return answer