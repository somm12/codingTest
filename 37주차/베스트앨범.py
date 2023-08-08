def solution(genres, plays):
    answer = []
    dict = {}
    count = {}
    for i,v in enumerate(genres):
        if v in dict:
            dict[v] += plays[i]
        else:
            dict[v] = plays[i]
            count[v] = 0
    arr = []
    
    for i in range(len(plays)):
        arr.append([dict[genres[i]], plays[i], i, genres[i]])
    arr.sort(key=lambda x:(-x[0],-x[1],x[2]))
    
    for v in arr:
        num,genre = v[2],v[3]
        if count[genre] >=2 :
            continue
        answer.append(num)
        count[genre] += 1
    return answer
# 프로그래머스 lv3 문제