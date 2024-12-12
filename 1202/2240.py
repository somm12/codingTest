n,m = map(int,input().split())
dp = [[[0 for _ in range(m+1)] for _ in range(2)] for _ in range(n+1)]
arr =[]
for _ in range(n):
    arr.append(int(input()))

def go(idx,tree,cnt):
    if cnt < 0: return -int(1e9)# 남은 횟수가 음수가 되는 경우 처리
    if idx == n: return 0# n번째 경우까지 왔을 때, 경우의 수는 마지막에 한 가닥이 남으므로 0을 반환.
    
    if dp[idx][tree][cnt]: return dp[idx][tree][cnt]
    dp[idx][tree][cnt] = max(go(idx+1, tree^1, cnt - 1),go(idx+1, tree,cnt)) + (tree == arr[idx] - 1) # 바꾼 경우,안바꾼 경우 재귀 호출 +(현재 상태값과 같은 경우 더하기)
    return dp[idx][tree][cnt]
    
print(max(go(0,0,m),go(0,1,m-1))) # tree 상태값을 0과 1로 둠.( 비트 연산 쉽게 하기 위해서 -1을 했음)
# 백준 자두나무
