n = int(input())
total = list(map(int,input().split()))

m = int(input())
arr = list(map(int,input().split()))
total.sort()

    
def check(target,start,end):
    while start <= end:
        mid = (start+end)//2
        if total[mid] == target:
            return True
        if total[mid] > target:
            end = mid - 1
        else:
            start= mid + 1
    return False

for v in arr:
    if check(v,0,n-1):
        print('yes',end=' ')
    else:
        print('no',end=' ')
# 이코테 이분탐색 예제