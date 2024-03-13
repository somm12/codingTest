def solution(cap, n, d, p):
    answer = 0
    while d and p and d[-1] == 0 and p[-1] == 0:
        d.pop()
        p.pop()
    while d or p:
        total = 0
        answer += (max(len(d),len(p))*2)# 둘 중에 더 남은 길이 긴 부분까지는 이동해야하므로 큰 길이 만큼 더하기
        while d:
            if total + d[-1] <= cap:
                total += d.pop()
            else:
                d[-1] -= (cap - total)
                break
        total = 0
        
        while p:
            if total+p[-1] <= cap:
                total += p.pop()
            else:
                p[-1] -= (cap - total)
                break
                
    return answer
# 뒤에서 부터 처리해야 최소 거리.