x,y = map(int,input().split())
s,e = 1,int(1e9)
ans = -1
prev =(y*100 // x)
while s<= e:
    mid = (s+e)//2
    nxt = ((y+mid)*100 // (x + mid))
    if nxt > prev:
        ans = mid
        e = mid-1
    else:
        s = mid + 1
print(ans)

# 백준 게임 문제.
# 선형적으로 찾으면 10억까지 갈 수 있으므로, 이분탐색 이용.