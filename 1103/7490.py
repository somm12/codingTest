tc = int(input())

def calc(res):
    res = res.replace(' ','')
    stk = []
    num = ''
    
    for v in res:
        if v.isdecimal():
            num += v
        else:
            stk.append(num)
            if len(stk) == 3:
                a = stk.pop()
                op = stk.pop()
                b = stk.pop()
                if op == '+':
                    stk.append(int(a) + int(b))
                else:
                    stk.append(int(b) - int(a))
            stk.append(v)
            num = ''
    stk.append(num)
    if len(stk) == 3: # 혹시 마지막 남은 수식의 길이가 1+2 와 같은 형태라면 계산하고, 하나라면 반환.
        a = stk.pop()
        op = stk.pop()
        b = stk.pop()
        if op == '+':
            stk.append(int(a) + int(b))
        else:
            stk.append(int(b) - int(a))
    
    return int(stk[0])

def go(L,res):
    
    if L == n:
        
        if calc(res) ==0:
            ans.append(res)
        return 

    go(L+1,res + '+' + str(L+1))
    go(L+1,res + '-' + str(L+1))
    go(L+1,res + ' ' + str(L+1))


for _ in range(tc):
    n = int(input())
    arr = [i for i in range(1,n+1)]
    ans = []
    go(1,'1')
    ans.sort()
    for v in ans:
        print(v)
    print()
    
# 백준 0만들기