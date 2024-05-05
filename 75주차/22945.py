n = int(input())
arr = list(map(int,input().split()))

l,e = 0,n-1

answer = 0
while l < e:
    a,b = arr[l],arr[e]
    value = (e-l-1)*min(a,b)
    answer = max(answer,value)
    if a < b:
        l += 1
    else:
        e -= 1
print(answer)
# A와B 사이의 수는 항상 답이 고정. 
# A와B의 능력치 최소값을 크게 만들기 위해서. 그 기준을 더 작은 값쪽에서 포인터 움직이기.