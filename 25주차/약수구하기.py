n, k = map(int,input().split())
dict = {}
for i in range(1, int(n**0.5)+1):
    if n % i == 0:
        dict[i]= 1
        dict[n//i] = 1
arr =list(dict.keys())
arr.sort() # k번째로 작은 수를 구하기 위해 정렬.

if len(dict) >=k:
    print(arr[k-1])
else:
    print(0)