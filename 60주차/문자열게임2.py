tc = int(input())
for _ in range(tc):
    w = input()
    k = int(input())
    minV = int(1e9)
    maxV = -1
    dict = {}
    for i in range(len(w)):
        s = w[i]
        if s not in dict:
            dict[s] = [i]
        else:
            dict[s].append(i)
    
    for s in dict:
        
        arr =dict[s]
        
        if len(arr) < k:
            continue
        
        for i in range(len(arr) - k + 1):
            minV = min(minV, arr[i+k-1] - arr[i]+1)
            maxV = max(maxV, arr[i+k-1] - arr[i]+1)
    if maxV == -1:
        print(-1)
    else:
        print(minV,maxV)
# 어떤 문자를 k개 포함한 가장 짧은 연속 문자열 길이 (결국 앞 뒤 문자가 같은 것.)
# 어떤 문자를 k개 포함하고, 앞 뒤 문자가 같은 가장 긴 연속 문자열 길이 
# 각 문자의 위치를 기록하고, k개 가 존재해야하므로, 각 문자가 위치한 인덱스를 구해서
# 해당 문자가 k개 이상 일때, 인덱스 값의 차이로 길이를 구할 수 있음.
