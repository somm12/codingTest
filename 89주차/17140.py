r,c,k = map(int,input().split())
A = []
for _ in range(3):
    A.append(list(map(int,input().split())))

r -= 1
c -= 1
t = 0

def rSort():
    res = []
    ms =0
    for arr in A:
        dict= {}
        for v in arr:
            if v == 0: continue
            if v in dict: 
                dict[v] += 1
            else:
                dict[v] = 1
        tmp = list(dict.items())
        tmp.sort(key= lambda x:(x[1],x[0]))
        row = []
        for key,item in tmp:
            row.append(key)
            row.append(item)
            
        if len(row) > 100:
            row = row[:100]
        res.append(row)
        ms= max(ms,len(row))
    result = []
    for row in res:
        if len(row) < ms:
            result.append(row + [0]*(ms-len(row)))
        else:
            result.append(row)
    return result

def cSort():
    res= []
    ms = 0
    n,m = len(A),len(A[0])
    for j in range(m):
        arr = []
        for i in range(n):# 열 부분을 행처럼 배열로 보기 쉽도록 옮기기.
            arr.append(A[i][j])
        dict = {}
        for v in arr:
            if v == 0: continue
            if v in dict: 
                dict[v] += 1
            else:
                dict[v] = 1
        tmp = list(dict.items())
        tmp.sort(key= lambda x:(x[1],x[0]))
        row = []
        for key,item in tmp:
            row.append(key)
            row.append(item)
            
        if len(row) > 100:
            row = row[:100]
        res.append(row)
        ms= max(ms,len(row))
    result = []
    for row in res:
        if len(row) < ms:
            result.append(row + [0]*(ms-len(row)))
        else:
            result.append(row)
   
    
    N,M = len(result[0]),len(result)
    B = [[0]*M for _ in range(N)]
    for x in range(M):
        for y in range(N):
            B[y][x]= result[x][y]
    return B
    
def inRange():
    n = len(A)
    m = len(A[0])
    return r < n and c < m
while True:

    if inRange() and A[r][c] == k:# r행c열 값이 k면 종료. 이전에 범위내에 해당하는지 확인.
        print(t)
        break
    if t == 100:# 100번 넘게 해도 안되면 -1
        print(-1)
        break
    if len(A) >= len(A[0]):# 행 기준 정렬.
        A= rSort()
    else:
        A = cSort()# 열 기준 정렬.
    t+= 1
