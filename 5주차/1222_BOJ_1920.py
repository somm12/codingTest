n = int(input())
arr1 = list(map(int, input().split()))
arr1.sort()
m = int(input())
arr2 = list(map(int, input().split()))

def bS (target, s, e):
    while s <= e:
        mid = ( s + e )//2
        if arr1[mid] == target:
            return 1
        if arr1[mid] > target:
            e = mid - 1
        else:
            s = mid + 1
    return 0

for i in arr2:
    print(bS(i, 0, n-1))