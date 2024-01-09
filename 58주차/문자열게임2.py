tc = int(input())
for _ in range(tc):
    w = input()
    k = int(input())
    ans1 = int(1e9)
    ans2 = 0

    dict = {}
    for i in range(len(w)):# 각 문자에 대해서 담긴 위치에 대한 배열 표현.
        if w[i] in dict:
            dict[w[i]].append(i)
        else:
            dict[w[i]] = [i]
    
    for x in dict:
        arr = dict[x]
        # 3번 수행도 결국 제일 짧은 길이를 구해야하므로, 시작과 끝 문자가 같아야함.
        for i in range(len(arr)-k+1):# 0이되면 반복문 실행을 안하므로, +1해주기.
            ans1 = min(ans1, arr[i+k-1]-arr[i]+1)# 끝idx - 시작idx + 1 => 길이 최대,최소 구하기.
            ans2 = max(ans2, arr[i+k-1]-arr[i]+1)
    if ans1 == int(1e9):# ans1 값이 없으면 ans2도 없다는 것.
        print(-1)
    else:
        print(ans1,ans2)