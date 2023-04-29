def dfs(res,end):
    arr.append(res)
    for i in range(end):
        dfs(res+str(i),i)

n = int(input())
arr = []
dfs('',10)
arr.sort(key=len)
if n >= len(arr):
    print(-1)
else:
    print(int(arr[n]))