n = int(input())
def check(s):
    index = -1
    for i ,v in enumerate(s):
        if v != '0':
            break
        else:
            index = i
    s = s[index+1:]
    return s

for _ in range(n):
    ans = ''
    a,b = map(str,input().split())

    a = check(a)
    b = check(b)
    
    tmp = ''
    if len(a) > len(b):
        b = b.rjust(len(a),'0')
        tmp= tmp.rjust(len(a),'0')
    else:
        a = a.rjust(len(b),'0')
        tmp= tmp.rjust(len(b),'0')
    
    tmp = list(tmp)
    
    for i in range(len(a)-1,-1,-1):
        v1,v2,v3 = a[i],b[i],tmp[i]
        cnt = (v1+v2+v3).count('1')

        if cnt == 0:
            ans += '0'
        elif cnt == 1:
            ans += '1'
        elif cnt == 2:
            if i == 0:
                ans += '01'
                break
            ans += '0'
            tmp[i-1] = '1'
        else:
            if i == 0:
                ans += '11'
                break
            ans += '1'
            tmp[i-1] = '1'
    if ans == '':
        print('0')
    else: print(ans[::-1])

# 아래 풀이는 bin 사용해서 빨리 푸는법.
for _ in range(n):
    a, b = input().split()
    a = int(a, 2) # -> 2진수를 십진수로 반환해줌.
    b = int(b, 2)
    print(bin(a+b)[2:])

