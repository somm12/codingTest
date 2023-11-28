import sys


tmp = set({'a','e','i','o','u'})
def printText(s, flag):
    if not flag:
        return '<' +s + '>'+ ' is not acceptable.'
    return '<' +s + '>'+ ' is acceptable.'
def check1():
    for v in s:
        if v in tmp:
            break
    else:# 난 하나도 모음이 없다면,
        return True
    return False

def check2():# 연속으로 모음 3개 또는 자음 3개가 나오는가.
    for i in range(len(s)-2):
        a = s[i:i+3]
        cnt1 = 0
        cnt2 = 0
        for v in a:
            if v in tmp:
                cnt1 += 1
                cnt2 =0
            else:
                cnt2 += 1
                cnt1 = 0
            if cnt1>=3 or cnt2>=3:
                return True
  
    return False
def check3():
    for i in range(0,len(s)-1):
        if s[i] == s[i+1]:
            if s[i] == 'o' or s[i] == 'e':
                continue
            else:
                return True
    return False

while (1):
    s = sys.stdin.readline().rstrip()
    
    if s== 'end':
        break
    if check1():
        print(printText(s,False))
        
    elif check2():
        print(printText(s,False))
        
    elif check3():
        print(printText(s,False))
        

    else:
        print(printText(s,True))
# 백준 문자열 문제