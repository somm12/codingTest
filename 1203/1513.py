n,m,c = map(int,input().split())
# 4차원 dp => x,y,cnt,prev (현재위치인 x,y, 오락실 개수인 cnt, prev는 순서를 지키기 위한 이전 오락실 번호를 담음)
dp = [[[[-1 for _ in range(51)] for _ in range(51)] for _ in range(m+1)] for _ in range(n+1)]
arr = [[0]*(m+1) for _ in range(n+1)]# 2차원 배열.

for i in range(1,c+1):
    x,y = map(int,input().split())
    arr[x][y] = i # 오락실 번호 할당.

def go(x,y,cnt,prev):
    if x > n or y > m:# 범위를 벗어나는 좌표 => 0. 경우의 수를 0으로 둬서 해당 경우 배제시킴.
        return 0
    if (x == n and y == m):
        if cnt == 0 and arr[x][y] == 0:# 학원에 도착 후, 그 위치에 오락실이 없는 경우.
            return 1
        elif cnt == 1 and arr[x][y] > prev:# 그 위치에 오락실이 있는 경우라면, 순서도 지켜야함.
            return 1
        return 0# 나머지는 배제.
    
    if dp[x][y][cnt][prev] != -1:# 해당 경우의 값이 이미 할당이 되었음.
        return dp[x][y][cnt][prev]
    
    dp[x][y][cnt][prev] = 0 # 값이 존재하지 않는 경우일 수 있기에 0을 할당.
    if arr[x][y] == 0:# 오락실이 없는 좌표.
        dp[x][y][cnt][prev] = (go(x+1,y,cnt,prev) + go(x,y+1,cnt,prev))% 1000007
    elif arr[x][y] > prev:# 오락실이 있는 좌표. 순서 지키기.
        dp[x][y][cnt][prev] = (go(x+1,y,cnt-1,arr[x][y]) + go(x,y+1,cnt-1,arr[x][y]))% 1000007
    
    return dp[x][y][cnt][prev]     

for i in range(c+1):
    print(go(1,1,i,0),end = ' ')
# 백준 경로찾기