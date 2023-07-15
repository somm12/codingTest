n,m = map(int,input().split())
arr = [i for i in range(1,n+1)]
for _ in range(m):
    i,j = map(int,input().split())
    i -= 1
    j -= 1
    prev = arr[:i]
    tmp = arr[i:j+1]
    tmp.reverse()
    after = arr[j+1:]
    arr = prev + tmp + after
   

for i in arr:
    print(i,end=' ')
