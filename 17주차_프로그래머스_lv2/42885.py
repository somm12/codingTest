def solution(people, limit):
    cnt = 0
    s = 0
    e = len(people) - 1
    people.sort()
    while s < e:
        if people[s] + people[e] <= limit:
            people[s] = 0
            people[e] = 0
            cnt += 1
            s += 1
            e -= 1
        else:
            e -= 1
    for i in people:
        if i != 0:
            cnt += 1
    
    return cnt
# 구명보트 - 투 포인터