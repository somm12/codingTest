n = int(input())
arr = list(map(int,input().split()))
def binary_search(start,end,target):
    if start > end:
        return start
       
    mid = (start+end) // 2
    
    if res[mid] > target:
        return binary_search(start,mid-1,target)
    elif res[mid] == target:
        return mid
    else:
        return binary_search(mid+1,end,target)

res = [arr[0]]

for i in range(1,len(arr)):
    
    if res[-1] < arr[i]:
        res.append(arr[i])
    else:
        idx = binary_search(0,len(res)-1,arr[i])

        res[idx] = arr[i]
  

print(len(res))
# dp로 풀면, 시간초과 발생. 이분탐색 사용.
# 각 숫자의 위치를 찾아가면서, 배열을 만든다. 마지막 배열의 길이가 가장 긴 길이.