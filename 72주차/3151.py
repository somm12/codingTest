from bisect import bisect_left
n = int(input())
arr = list(map(int,input().split()))
arr.sort()
answer = 0
for i in range(n-2):
    l = i
    ln = i+1
    r = n-1
    while ln < r:
        total = arr[l]+ arr[ln] + arr[r]
        if total > 0:
            r -= 1
        else:
            if total == 0:
                if arr[r] == arr[ln]:#값이 같다면, 개수 뺀만큼 더하기.
                    answer += (r-ln)
                else:# 다르다면, r쪽에서 같은 숫자 몇개인지 구하기. 
                    k = bisect_left(arr,arr[r])
                    answer += (r-k+1)

        
            ln += 1
print(answer)