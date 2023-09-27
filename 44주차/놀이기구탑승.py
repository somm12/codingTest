dx = [-1,1,0,0]
dy = [0,0,-1,1]
answer = 0
n = int(input())
g = [[0]*n for _ in range(n)]
dict = {}

for _ in range(n*n):
    n0,n1,n2,n3,n4 = map(int,input().split())
    dict[n0] = [n1,n2,n3,n4]# n0가 좋아하는 4명을 딕셔너리 dict에 담기.

def go():# 놀이기구 탑승할 위치 정하는 함수. (인접 4칸에 좋아하는 사람 수 많고 > 인접칸에 빈칸이많고 > 행이 작고 > 열이 작고)
    global g
    cand = []
    for x in range(n):
        for y in range(n):
            if g[x][y] == 0:
                empty = 0
                like = 0
                for i in range(4):
                    nx = x+dx[i]
                    ny = y +dy[i]
                    if 0 <= nx < n and 0 <= ny < n:
                        if g[nx][ny] in dict[now]:
                            like += 1
                        elif g[nx][ny] == 0:
                            empty +=1
                cand.append((like,empty,x,y))
    cand.sort(key=lambda x:(-x[0],-x[1],x[2],x[3]))

    a,b = cand[0][2], cand[0][3]# 조건에 가장 부합하는 좌표에 할당.
    g[a][b] = now

for now in dict:
    go()
# 총 점수 구하기.
for x in range(n):
    for y in range(n):
        cnt = 0
        num = g[x][y]
        for i in range(4):# 인접 4칸에 좋아하는 사람 수에 따라서 점수 더하기.
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0 <= ny < n and g[nx][ny] in dict[num]:
                cnt += 1
        answer += int(10**(cnt-1)) # 0명은 0점, 1명은 1점,2명은 10점, 3명은 100점, 4명은 1000점
print(answer)
# 삼성 기출