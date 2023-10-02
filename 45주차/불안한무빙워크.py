from collections import deque

nth = 1
n,k = map(int,input().split())
arr = list(map(int,input().split()))
q = deque(arr)# 내구성을 나타내는 큐
p = [0]*n# 사람 존재 여부를 나타내는 큐
p = deque(p)

def rotate():# 회전.
    global q,p
    p.rotate(1)
    q.rotate(1)
    if p[n-1] == 1:# n번째 칸에 도달시 즉시 내림.
        p[n-1] = 0

def move():# 1칸 이동
    global q,p
    for i in range(n-2,-1,-1):
        if p[i] == 1:
            if q[i+1] > 0 and p[i+1] == 0:# 다음칸 내구성이 0이 아니고, 누가 없다면 이동.
                p[i+1] = 1
                p[i] = 0 
                q[i+1] -= 1 # 이동시 내구성 -1
    if p[n-1] == 1:# n번째 칸 도달시 즉시 내림.
        p[n-1] = 0
def getOn():# 1번째 칸에 내구도가 0 이 아니고 아무도 없다면, 올라감.
    global q,p
    if p[0] == 0 and q[0] > 0:
        p[0]=1 # 올라갈 때 내구성 -1
        q[0] -=1
def isDone():# 내구성이 0 인 칸이 k개이상일 시 종료
    cnt = 0
    for v in q:
        if v == 0:
            cnt += 1
    if cnt >= k:
        return True
    return False

while True:
    rotate()
    move()
    getOn()
    if isDone():
        break
    nth += 1
print(nth) # 종료조건에 해당 되는 때가 몇 번째인지 체크.