tc = int(input())

for _ in range(tc):
    s = input()
    n = len(s)
    l = 0 # 왼쪽, 오른쪽 투 포인터 이용.
    r = len(s) - 1
    answer =0
    for i in range(n):
        if s[l] == s[r]:
            l += 1
            r -= 1
            continue
        else:
            if s[l+1] == s[r]:# 만약 왼쪽 부분을 빼고 같은지 확인
                tmp = s[l+1:r+1]
                if tmp[:] == tmp[::-1]:
                    answer = 1
                    break
            if s[l] == s[r-1]:# 오른쪽 부분 빼고 같은지 확인.
                tmp = s[l:r]
                if tmp[:] == tmp[::-1]:
                    answer = 1
                    break
            answer = 2
            break
    print(answer)
