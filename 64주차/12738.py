n = int(input())
arr =list(map(int,input().split()))
res = []

def find(s,e,v):
    while s <= e:
        mid = (s+e)//2
        if res[mid] == v:
            return mid
        if res[mid] < v:
            s = mid+1
        else:
            e = mid - 1
    return s

for v in arr: 
    if len(res) == 0:
        res.append(v)
        continue
    idx = find(0,len(res)-1,v)
    if idx >= len(res):
        res.append(v)
    else:
        res[idx] = v
print(len(res))
print(res)