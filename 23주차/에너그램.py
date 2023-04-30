def dfs(L,res):
    if L == len(arr):
        print(''.join(res))
        return
    for v in check:
        if check[v]:
            check[v] -= 1
            dfs(L+1,res+[v])
            check[v] += 1
        
            
n = int(input())
for _ in range(n):
    arr = list(input())
    arr.sort()
    check = {}
    for i in arr:
        if i not in check:
            check[i] = 1
        else:
            check[i] += 1
    dfs(0,[])
