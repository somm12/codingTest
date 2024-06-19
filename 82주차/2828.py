n,m = map(int,input().split())
cnt = int(input())
l = 1
answer = 0
for _ in range(cnt):
    p = int(input())
    r = l+m - 1 # m칸을 차지하므로, 가장 오른쪽 칸 계산.
    if l <= p <= r:# 현재 바구니 내에 들어온다면 그대로.
        continue
    elif p > r:# 바구니의 오른쪽 위치에 내려올 때. 가장 오른쪽 칸을 기준으로 이동하여 최소 이동거리 계산.
        answer += (p-r)
        l += (p-r)
    elif p < l:# 바구니의 왼쪽 위치 => 가장 왼쪽 칸을 기준으로 이동해서 최소 이동거리 계산
        answer += (l-p)
        l -= (l-p)
print(answer)
# 백준 사과 담기 게임