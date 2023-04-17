import collections

def solution(cards):
    leng = len(cards)
    unvisited = [True]*leng
    scores = collections.Counter()
    
    for i in range(leng):
        if unvisited[i] == True:
            scores[i] = 0
            pos = i
            while True:
                unvisited[pos] = False
                pos = cards[pos] - 1
                scores[i] += 1
                if unvisited[pos] == False:
                    break
    # 데이터의 개수가 많은 순으로 정렬된 배열을 리턴               
    answer = scores.most_common(2)
    
    if len(answer) == 1:
        return 0
    else:
        return (answer[0][1]*answer[1][1])
    
# 원소의 개수가 가장 큰 두 집합을 알아내는 문제