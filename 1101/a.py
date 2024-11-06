arr = []
def dfs(L,res,start):
    if len(res) == 3:
        arr.append(res)
        return

    for i in range(start,4):
        dfs(L+1,res+[i],i+1)

dfs(0,[],0)
print(arr)