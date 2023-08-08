
s = int(input())
start = 1
end = s
answer = 0
while(start <= end):
    mid = (start+end)//2

    total = (mid*(mid+1))//2
    if s >= total:
        answer = mid
        start = mid+1
    else:
        end = mid-1
        
print(answer)
# 백준 이분탐색 문제