from collections import deque

def solution(n, m, x, y, r, c, k):
    answer = ''
    # 최단거리 계산
    def calc(x1, y1):
        return abs(x1 - (r-1)) + abs(y1-(c-1))

    # k가 최단 거리보다 작거나, 최단 거리 이후 남은 거리 값이 홀수라면 k번으로 도착 불가
    if calc(x-1, y-1) > k or (calc(x-1, y-1) - k) % 2:
        return 'impossible'
    # 탐색 방향 사전순으로 - d l r u ***!
    direct = {(1,0):'d', (0,-1):'l', (0,1):'r', (-1,0):'u'}
    q = deque()
    q.append((x-1, y-1, 0, ''))
    while q:
        x, y, cnt, route = q.popleft()
        # 도착했는데 남은 거리가 홀수라면 도착지에 k만큼 오지 못함. 짝수만큼 왔다갔다할 수 있다.
        if (x, y) == (r-1, c-1) and (k-cnt) % 2:
            return 'impossible'
        elif (x, y) == (r-1, c-1) and cnt == k:
            return route
        for di, dj in direct:
            ni, nj = x+di, y+dj
            if 0<=ni<n and 0<=nj<m:
                # 다음 이동했을 때, k만큼 갈 수 있느냐 체크.
                # 이동 했을 때 거리: cnt+1, 그 지점으로 부터 최단 거리 calc(ni,nj)
                if calc(ni, nj) + cnt + 1 > k:
                    continue
                q.append((ni, nj, cnt+1, route+direct[(di, dj)]))
                break# 현재 x,y 지점 일 때의 최선의 이동 방향이므로, break로 끊어내기.

    return answer
# 프로그래머스 .