while True:
    try:
        v = input()
        s,t = v.split(' ')
        l = 0
        for i in range(len(t)):
            if l >= len(s):
                break
            if s[l] == t[i]:
                l += 1
        if l >= len(s):# t내에 s가 부분 문자열로 존재한다면, l 의 값은 len(s)이상 일 것.
            print('Yes')
        else:
            print('No')
    except EOFError:
        break
