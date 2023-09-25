n,m = map(int,input().split())
tree = []
for _ in range(n):
    tree.append(list(map(int,input().split())))

dx = [0,-1,-1,-1,0,1,1,1]# 1~8부터 입력 받은 방향.
dy = [1,1,0,-1,-1,-1,0,1]

answer =0
pill = {}# 영양제가 위치한 좌표를 담을 딕셔너리.
for x in [n-1,n-2]:# 초기에는 좌하단에 4칸에 존재.
    pill[(x,0)]=1
    pill[(x,1)]=1

def pillMove():# 영양제 이동. d방향, p칸만큼 ** 행과 열은 연결되어있음!
    global pill
    tmp = {}
    for x,y in pill:
        nx = (x + (dx[d]*p))%n
        ny = (y + (dy[d]*p))%n
        tmp[(nx,ny)]=1
    pill = tmp

def givePill():# 영양제 투입 -> 나무 높이 + 1.
    global tree
    for x,y in pill:
        tree[x][y] +=1
def cross():# 영양제가 있는 칸에서 , 각 대각선 4방향 인접칸에 나무 높이가 1인상인 것 개수 만큼 나무 높이 증가.
    global tree
    for x,y in pill:
        cnt =0
        for i in [1,3,5,7]:# 대각선 4방향 인덱스들.
            nx = x+dx[i]
            ny = y+dy[i] # 격자 범위를 벗어나는 건 제외.
            if 0 <= nx < n and 0 <= ny < n and tree[nx][ny] >= 1:
                cnt +=1
        tree[x][y] += cnt

def newPill():# 현재 영양제 위치 제외한 곳에서, 높이가 2이상인 곳에 영양제 배치, 높이도 -2.
    global tree,pill
    tmp = {}
    for x in range(n):
        for y in range(n):
            if (x,y) not in pill:
                if tree[x][y] >= 2:
                    tree[x][y] -= 2
                    tmp[(x,y)] =1
    pill = tmp

for _ in range(m):
    d,p = map(int,input().split())
    d -=1

    pillMove()
    givePill()
    cross()
    newPill()


for v in tree:# 총 나무 높이 합.
    answer += sum(v)
print(answer)

# 삼성 기출.