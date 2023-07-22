r,c,k = map(int,input().split())
A= []
for _ in range(3):
    A.append(list(map(int,input().split())))
time =0
r -= 1
c -= 1

def sortMatrix(x): # R / C 연산을 해서. 정렬
    global A
    if x == 'C':
        A = list(zip(*A)) # 열마다 정렬을 쉽게 하기 위해서 zip 연산을 써서 행과 열을 바꿈.
    new = [] # 정렬된 결과를 담을 배열.
    long = -1 # 가장 큰 행/열을 길이를 담을 변수.
    for arr in A:
        tmp = [] # 정렬을 하기위해 임시 저장소로 사용될 변수
        for v in set(arr):
            if v == 0: # 0은 정렬에 포함하지 않음
                continue
            cnt = arr.count(v)
            tmp.append([v,cnt])
        tmp.sort(key = lambda x : (x[1],x[0])) # 횟수가 커지는 순 다음으로 숫자가 커지는 순으로 정렬.
        sortedRow = [] # 각 행이 정렬된 정보를 1차원 배열 형태로 임시 저장될 배열.
        for i in tmp:
            sortedRow += i # [숫자, 개수] 형태로 빈배열에 더해짐.
        new.append(sortedRow)
        long = max(long, len(sortedRow))
    
    for arr in new:
        if len(arr) < long:
            arr += [0]*(long- len(arr)) # 가장 큰 행 기준으로 0을 채우기.
    if x == 'C':
        A = list(zip(*new)) # 다시 원래 형태의 배열로 zip연산해주기.
    else:
        A = new

while True:
    # 배열의 형태가 바뀌기 때문에, A[r][c] 값을 확인시, 범위도 확인.
    if 0<= r < len(A) and 0 <= c < len(A[0]) and A[r][c] == k:
        print(time)
        break
    if time > 100:# 100초 넘어가면 -1 출력.
        print(-1)
        break
    row = len(A)
    col = len(A[0])

    if row >= col: # 행 >= 열이면 R연산
        sortMatrix('R')
    else:
        sortMatrix('C')
    
    if len(A) > 100 or len(A[0]) > 100: # 크기가 100 넘어가면 100x100으로 자르기.
        tmp = []
        for i in range(len(A)):
            if i < 100:
                tmp.append(A[i][:100])
            else:
                break
        A = tmp
    time += 1