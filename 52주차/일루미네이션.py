from collections import deque


w,h = map(int,input().split())
g = [[0 for _ in range(w+2)] for _ in range(h+2)]

answer =0
for i in range(1,h+1):
    g[i][1:w+1] = map(int,input().split())


dy = [-1,1,0,0,-1,1]# 행부분. 
dx = [[0,0,-1,1,-1,-1],[0,0,-1,1,1,1]]#열 부분. 행의 인덱스 번호가 짝수 일 때. 홀수 일 때 경우 다름.
# 상좌 하좌, 상우 하우
def bfs(x,y):
    global answer
    visited = [[0 for _ in range(w+2)] for _ in range(h+2)] # 방문체크 배열 생성
    visited[y][x] =1
    q = deque()
    q.append((y,x))
    while q:
        y,x = q.popleft()
        for i in range(6):
            ny,nx = y+dy[i],x+dx[y%2][i]
            if 0<= ny < h+2 and 0<= nx < w+2:
                if g[ny][nx] == 0 and not visited[ny][nx]:
                    visited[ny][nx]= 1
                    q.append((ny,nx))
                if g[ny][nx] == 1:
                    answer += 1
       
bfs(0,0)
print(answer)
# 백준 그래프탐색
# 테두리에 0으로 초기화.
# 0을 위주로 탐색하면서 맞닿은 1을 개수를 구한다. -> 1로 둘러쌓인 0은 신경 안써도 됨.