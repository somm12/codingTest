n = int(input())
arr = list(map(int,input().split()))

def binary_left(arr,target):
    s = 0
    e = len(arr)-1
    while s <= e:
        mid = (s+e)//2
        if arr[mid] <= target:
            s = mid + 1
        else:
            e = mid - 1
    return s
            

tmp = []

for v in arr:
    
    if len(tmp) == 0 or tmp[-1] < v:# 가장 큰 값보다 큰 값이 들어오면 append
        tmp.append(v)
    else:# 해당 위치에 값 넣기.
        idx = binary_left(tmp,v)
        tmp[idx] = v
print(len(tmp))
# 백준 가장 긴 부분 증가 수열.
# 이분 탐색을 통해 끼어들 수 있는 가장 왼쪽 인덱스를 찾아서, 수열을 만들어나간다.