def solution(s, skip, index):
    ans = []
    arr = []
    for i in range(26):
        c = chr(97+i)
        if c not in skip:
            arr.append(c)
            
    for i in s:
        ans.append(arr[(arr.index(i)+index) % len(arr)])
    ans = ''.join(ans)
    return ans
# 둘만의 암호
# 배열.index(문자) => 그 배열 내에서 해당 문자의 인덱스 반환. 중복된 문자 일시, 제일 앞 인덱스 반환.