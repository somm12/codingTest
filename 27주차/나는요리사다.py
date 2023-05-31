arr = []
for i in range(5):
    arr.append(list(map(int,input().split())))
    arr[i].append(i+1)

arr.sort(key=lambda x : sum(x[:4]))
print(arr[4][4],sum(arr[4][:4]))