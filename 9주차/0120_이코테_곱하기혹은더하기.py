arr = list(map(int,input()))
res = arr[0]
for i in range(len(arr)-1):
    plus = res + arr[i+1]
    multiply = res*arr[i+1]
    res = max(plus, multiply)

print(res)

# 방법2 : 결과 혹은 값이 0 이나 1이면 곱하는 것이 숫자가 더 커짐.
for i in range(1,len(arr)):
    if res <= 1 or arr[i]<=1:
        res += arr[i]
    else:
        res *= arr[i]