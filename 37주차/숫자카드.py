n = int(input())
card = list(map(int,input().split()))
card.sort()

m = int(input())
arr = list(map(int,input().split()))

def check(target,start,end):
    while start <= end:
        mid = (start+end)//2
        if target == card[mid]:
            return True
        
        if target < card[mid]:
            end = mid-1
        else:
            start = mid+1
    return False

for v in arr:
    if check(v,0,n-1):
        print(1,end=' ')
    else:
        print(0,end=' ')
