def solution(line):
    answer = []
    cross = {}
    for i in range(len(line)):
        for j in range(i+1, len(line)):
            a,b,e = line[i]
            c,d,f = line[j]
            if (a*d - b*c) != 0:
                x = (b*f -e*d)/(a*d - b*c)
                y = (e*c - a*f)/(a*d - b*c)
                if int(x) == x and int(y) == y:
                    cross[(int(x),int(y))] = 1
    arr = list(cross.keys())
    arr.sort(key=lambda x: -x[0])
    maxX = arr[0][0]
    minX = arr[len(arr)-1][0]
    
    arr.sort(key=lambda x: -x[1])
    maxY = arr[0][1]
    minY = arr[len(arr)-1][1]
    col = maxY-minY+1
    g = [['.']*(maxX - minX + 1) for _ in range(col)]
    new = []
    # 행,열이 음수가 되지 않게 계산
    for i,j in arr:
        nx = maxY - j
        ny = i - minX
        new.append((nx,ny))
    
    for x,y in new:
        g[x][y] = '*'
    for i in g:
        i = ''.join(i)
        answer.append(i)
    return answer