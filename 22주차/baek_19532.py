def dfs(L):
    if L == 2:
        x = res[0]
        y = res[1]
        tmp1 = a*x + b*y
        tmp2 = d*x + e*y
        if tmp1 == c and tmp2 == f:
            print(x,y)
        return
    for i in range(-999,1000):
        res.append(i)
        dfs(L+1)
        res.pop()

res = []
a,b,c,d,e,f = map(int,input().split())
dfs(0)

# 다른 풀이.
for x in range(-999,1000):
    for y in range(-999,1000):
        if a*x + b*y == c and d*x+e*y == f:
            print(x,y)
            break