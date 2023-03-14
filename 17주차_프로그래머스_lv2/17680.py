def solution(cacheSize, cities):
    answer = 0
    q = []
    if cacheSize == 0:
        return len(cities)*5
    for city in cities:
        city = city.lower()
        if city in q:
            q.remove(city)
            q.append(city)
            answer += 1
        else:
            answer += 5
            if len(q) >= cacheSize:
                q.pop(0)
                q.append(city)
            else:
                q.append(city)
            
    return answer
# 캐시 : LRU 알고리즘