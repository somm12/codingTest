T = int(input())
for _ in range(T):
    n = int(input())
    arr1 = set(list(map(int,input().split())))
    m = int(input())
    arr2 = list(map(int,input().split()))
    for v in arr2:
        if v in arr1:
            print(1)
        else:
            print(0)