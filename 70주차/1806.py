answer = int(1e9)
n,s = map(int,input().split())
e = 0
arr =list(map(int,input().split()))
total = 0
for start in range(n):
    while total < s and e < n:
        total += arr[e]
        e += 1
    if total >= s:# 합이 s이상이라면, 최소 길이를 구하는 것이므로 짜르기.
        print(start,e)
        answer = min(answer,e-start)
    
    total -= arr[start]

if answer == int(1e9):# 합이 s이상이 되는경우가 아예없다면, 0 출력
    print(0)
else:
    print(answer)