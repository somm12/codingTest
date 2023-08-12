def solution(routes):

    routes.sort(key=lambda x:x[1])
    x = routes[0][1]
    cnt =1
    for s,e in routes:
        if s <= x <=e:
            continue
        else:
            x = e
            cnt += 1
    
            
    return cnt

# 프로그래머스 lv3 문제.