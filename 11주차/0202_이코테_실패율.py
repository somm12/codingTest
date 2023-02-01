def solution(n,stages):
    res = []
    temp = [0] * (n+1+1)
    for data in stages:
        temp[data] += 1
    total = sum(temp)
    for i in range(1,n+1):
        if temp[i] == 0:
            res.append((0,i))
        else:
            res.append((temp[i]/total,i))
        total -= temp[i]
    
    res.sort(key=lambda x:(-x[0],x[1]))
    result = []
    for d in res:
        result.append(d[1])
    return result