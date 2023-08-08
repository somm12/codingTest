n,m = map(int,input().split())
arr = list(map(int,input().split()))
maxV = max(arr)

answer =0
def sol(start,end):
    global answer
    while start <= end:
        mid = (start+end)//2

        cnt = 0
        for v in arr:
            if v > mid:
                cnt +=(v-mid)
            
        if cnt < m:
            end = mid - 1
        else:
            start = mid + 1
            answer = mid
    
sol(0,maxV)
print(answer)
# 이코테 이분탐색 예제