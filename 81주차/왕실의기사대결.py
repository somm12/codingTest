from collections import deque
dx = [-1,0,1,0]
dy = [0,1,0,-1]

L,N,Q = map(int,input().split())
g = []
for _ in range(L):
    g.append(list(map(int,input().split())))
p = {}
area =[[0]*L for _ in range(L)]
for i in range(1,N+1):
    r,c,h,w,k = map(int,input().split())
    r -= 1
    c -= 1
    p[i] = [r,c,h,w,k]
    for a in range(r,r+h):
        for b in range(c,c+w):
            area[a][b] = i

def inRange(x,y):
    return 0 <= x< L and 0 <= y < L

def move(idx,d):
    global area, p
    q = set()# 큐 역할을 하지만, 중복되는 부분 제거를 위해 set사용.
    q.add(idx)
    arr =set()# 움직이게되는 기사 번호 정보.
    arr.add(idx)
    while q:
        num = q.pop()

        x,y,h,w,k = p[num]
        for i in range(x,x+h):
            for j in range(y,y+w):
                nx,ny = i+dx[d],j+dy[d]
                if not inRange(nx,ny) or g[nx][ny] == 2:
                    return False # 이동할 칸이 벽을 만난다면 모두 이동 불가.
                # 중복을 막기위해 이미 움직이게되는 기사 번호를 확인했다면 넘기기.
                if area[nx][ny] not in arr and area[nx][ny] != 0:# 누가 있다면, 연쇄적으로 밀릴 수 있음.
                    arr.add(area[nx][ny])
                    q.add(area[nx][ny])

    # 이동 처리.
    newArea = [[0]*L for _ in range(L)]

    for num in arr:# 기사 정보 수정.
        x,y,h,w,k = p[num]
        nx,ny = x+dx[d],y+dy[d]
        p[num] = [nx,ny,h,w,k]
    for num in p:# 수정 후 새로, 면적 정보 업데이트.
        x,y,h,w,k = p[num]
        for i in range(x,x+h):
            for j in range(y,y+w):
                newArea[i][j] = num
    area = newArea
    return arr

def demage(moving):
    global p,area,info
    tmp = {}
    disAppear = set()
    for num in p:# 기사들 중.
        if num in moving:# 움직이는 기사.
            cnt = 0
            x,y,h,w,k = p[num]
            if num == idx:#명령받은 기사는 피해 없음.
                tmp[num] = p[num]
                continue
            for a in range(x,x+h):
                for b in range(y,y+w):
                    if g[a][b] == 1:
                        cnt += 1
            if k > cnt:
                tmp[num] = [x,y,h,w,k-cnt]
            else:
                disAppear.add(num)
            
            info[num] += cnt# 피해 총합 업데이트.
        else:# 움직이지 않는 기사
            tmp[num] = p[num]# 그대로.

    # 사라진 기사 반영.
    for num in disAppear:
        x,y,h,w,_ = p[num]
        for i in range(x,x+h):
            for j in range(y,y+w):
                area[i][j] = 0
    p = tmp


info = [0]*(N+1)
for t in range(1,Q+1):
    idx,d =map(int,input().split())
    if idx not in p:# 명령 무시.
        continue

    ret =move(idx,d)# 이동하게 되는 기사 번호 set 반환.
   
    if ret == False:# 이동을 못하게 된다면.
        
        continue# 손해 발생 없음.
    else:
        demage(ret)
        
answer =0
for num in p:
    answer += info[num]
print(answer)
# 코드트리.

