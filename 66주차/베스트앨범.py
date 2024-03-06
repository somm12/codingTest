def solution(genres, plays):
    answer = []
    dict = {}
    info = {}
    for i in range(len(genres)):
        if genres[i] in dict:
            dict[genres[i]] += plays[i]
            info[genres[i]].append((plays[i],i))
        else:
            dict[genres[i]] = plays[i]
            info[genres[i]] = [(plays[i],i)]
    arr = list(dict.items())
    arr.sort(key = lambda x: -x[1])
  
    for gen,cnt in arr:
        tmp = info[gen]
        tmp.sort(key = lambda x:(-x[0],x[1]))
        tmp = tmp[:2]
        for cnt, idx in tmp:
            answer.append(idx)
            
    return answer