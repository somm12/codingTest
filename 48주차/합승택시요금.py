INF = int(1e9)
def solution(n, s, a, b, fares):
    answer = 0
    g = [[INF]*(n+1) for _ in range(n+1)]
    
    for c,d,f in fares:
        g[c][d] = f
        g[d][c] =f 
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i ==j:
                g[i][j] = 0
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                g[i][j] = min(g[i][j], g[i][k]+g[k][j])
                
    answer = g[s][a] + g[s][b]# 합승없이 타는경우.
    for num in range(1,n+1):
        tmp = g[s][num] +g[num][a] + g[num][b]
        answer = min(answer,tmp)
            
        
    return answer
#프로그래머스
#플로이드워셜.
# 모든 중간지점 + 각 a,b까지 최소비용 최솟값.