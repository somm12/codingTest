n = int(input())
for _ in range(n):
    s= input()
    dict = {}
    for v in s:
        if not v.isalpha():
            continue
        if v in dict:
            dict[v] += 1
        else:
            dict[v] =1
    arr =list(dict.items())
    arr.sort(key = lambda x: -x[1])
    a,cnt = arr[0]
    if len(arr) > 1 and arr[1][1] == cnt:
        print("?")
    else:
        print(a)