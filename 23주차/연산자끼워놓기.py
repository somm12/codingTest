
def calc(res,a):
    tmp = a[0]
    for i,v in enumerate(res):
        if v == 0:
            tmp += a[i+1]
        elif v == 1:
            tmp -= a[i+1]
        elif v == 2:
            tmp *= a[i+1]
        else:
            if tmp < 0:
                tmp = abs(tmp) // a[i+1]
                tmp *= -1
            else:
                tmp //= a[i+1]
    return tmp
def dfs(res,arr,n,a):
    global maxV,minV
    if len(res) == n-1:
        v = calc(res,a)
        maxV = max(maxV,v)
        minV = min(minV,v)
        return
    for i,v in enumerate(arr):
        if v > 0:
            arr[i] -= 1
            dfs(res+[i],arr,n,a)
            arr[i] += 1
        
n = int(input())
a = list(map(int,input().split()))
arr = list(map(int,input().split()))
maxV = -int(1e9)
minV = int(1e9)
dfs([],arr,n,a)
print(maxV)
print(minV)