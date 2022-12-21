n = int(input())
arr1 = list(map(int, input().split()))
arr1.sort()
m  = int(input())
arr2 = list(map(int, input().split()))

def bi_s(x, s, e):
    
    while s <= e:
        mid = (s+e)//2
        if arr1[mid] == x:
            return 'yes'
        if arr1[mid] < x:
            s = mid + 1
        else:
            e = mid - 1
    return 'no'

for i in arr2:
    print(bi_s(i, 0, n - 1),end=' ')
        