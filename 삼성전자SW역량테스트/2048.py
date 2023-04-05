import copy
n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int,input().split())))
direction = [(-1,0),(1,0),(0,-1),(0,1)]
answer = -1
def perm(a,L):
    res = []
    def permute(arr):
        if len(arr) == L:
            res.append(arr)
            return
        for i,v in enumerate(a):
            permute(arr+[v])
    permute([])
    return res

def max_block(b):
    global answer
    for i in range(n):
        for j in range(n):
            answer = max(b[i][j],answer)


def move(tmp,d):
    a = []
    check = [[0]*n for _ in range(n)]
    if d % 2 == 0:# 상 or 좌.
        for i in range(n):
            for j in range(n):
                if tmp[i][j] != 0:
                    a.append((i, j))
    else:
        for i in range(n-1,-1,-1):
            for j in range(n-1,-1,-1):
                if tmp[i][j] != 0:
                    a.append((i, j))
    for x,y in a:
        nx = x
        ny = y

        nothing =False
        while True:
            nx += direction[d][0]
            ny += direction[d][1]
            if 0 <= nx < n and 0<= ny < n:
                if tmp[nx][ny] == 0:
                    continue
                elif tmp[nx][ny] == tmp[x][y] and not check[nx][ny]:
                    tmp[nx][ny] *= 2
                    tmp[x][y] = 0
                    check[nx][ny] = 1
                    break
                else:
                    nothing = True
                    break
            else:
                nothing = True
                break

        if nothing:
            nx -= direction[d][0]
            ny -= direction[d][1]
            if (nx,ny) != (x,y):
                tmp[nx][ny] = tmp[x][y]
                tmp[x][y] = 0

    return tmp


for case in perm([0,1,2,3],5):#[[1,1,1,1,1]]
    tmp = copy.deepcopy(board)
    for idx in case:# [상,하,좌,상]을 나타내는 인덱스.
        new = move(tmp,idx)
        tmp = new
    max_block(tmp)
print(answer)