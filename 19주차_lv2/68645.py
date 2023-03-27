def solution(n):
    answer = []
    arr = [[0]*i for i in range(1,n+1)]
    cnt = 1
    nx = 0
    ny = 0
    arr[0][0] = 1
    dx = [1,0,-1]
    dy = [0,1,-1]
    while True:
        if cnt == n*(n+1) // 2:
            break
        else:
            for i in range(3):
                while True:
                    nx += dx[i]
                    ny += dy[i]
                    if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 0:
                        cnt += 1
                        arr[nx][ny] = cnt
                    else:
                        nx -= dx[i]
                        ny -= dy[i]
                        break
    for i in arr:
        for j in i:
            answer.append(j)

    return answer
# 삼각 달팽이