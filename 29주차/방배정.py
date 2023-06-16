g = [0]*7
b = [0]*7

n,k = map(int,input().split())
def countRoom(arr):
    ans = 0
    for i in arr:
        if i%k > 0:
            ans += (i//k) + 1
        else:
            ans += (i//k)
    return ans
for _ in range(n):
    s,y = map(int,input().split())
    if s == 1:
        b[y] += 1
    else:
        g[y] += 1
answer = 0

answer += countRoom(g)
answer += countRoom(b)
print(answer)