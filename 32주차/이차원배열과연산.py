r,c,k = map(int,input().split())
matrix = []
r -= 1
c -= 1

for _ in range(3):
    matrix.append(list(map(int,input().split())))

def sortMatrix(matrix, cal):
    new = [] # 정렬된 모습을 담을 배열.
    maxLength = -1 # 가장 큰 row의 길이를 담을 변수.
    for row in matrix:
        info = [] # 각 row의 (숫자, 개수) 형태를 담을 배열.
        sortedRow = [] # 개수 > 숫자 가 커지는 순으로 정렬된 형태를 담을 배열.
        for num in set(row): # 중복을 없애고, 각 숫자가 row에서 몇개가 있는지 count를 이용.
            if num == 0: # 0인 것은 무시.
                continue
            cnt = row.count(num)
            info.append((num,cnt))
        
        info.sort(key=lambda x: (x[1],x[0])) # 개수 > 숫자 가 커지는 순으로 정렬하기
        
        for num, cnt in info:
            sortedRow += [num,cnt] # 해당 row가 정렬된 형태를 담는다.
        new.append(sortedRow) # 정렬된 row를 새로운 배열에 담기.
        maxLength =max(maxLength, len(sortedRow)) # row중에서 최대 길이를 구한다.
    
    # 변한 것은 row만 변했기 때문에, 
    # 0을 추가하는 것과 100개가 넘으면 자르는 것도 row만 수행!
    for row in new:
        row += [0] * (maxLength-len(row)) # 가장 큰 행 길이에 맞춰서 0을 채운다.
        if len(row) > 100: # 행 길이가 100 넘으면 자르기!
            row = row[:100]
    if cal == 'R':# R연산이라면, 그대로 반환.
        return new
    else: # C연산이면, 다시 행 형태를 열로 되돌림.
        return list(zip(*new))

time = 0
while True:
    if time > 100: # 100초 넘으면 -1 출력.
        print(-1)
        break
    # r행,c열 에 값이 k가 되면 멈추기.
    if 0 <= r < len(matrix) and 0 <= c < len(matrix[0]) and matrix[r][c] == k:
        print(time)
        break
    # 행 개수 >= 열개수면, R 연산하기(행을 중심으로 정렬)
    if len(matrix) >= len(matrix[0]):
        matrix = sortMatrix(matrix,'R')
    else: # 행 개수 < 열개수면, C 연산하기(열을 중심으로 정렬)
        matrix = sortMatrix(list(zip(*matrix)),'C') # zip*을 사용하면, 행을 열로 바꾼 형태로 만들어 준다.!!!!
    time +=1
    
# zip(* array) 형태를 이용하면 쉽게 행을 열형태로 바꿔줌
# set을 사용하여 중복제거
# count사용해서 해당 배열에서 숫자 개수 세기

