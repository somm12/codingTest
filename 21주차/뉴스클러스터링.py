def solution(str1,str2):
    answer = 0
    s1 = str1.lower()
    s2 = str2.lower()
    a = []
    b = []
    for i in range(len(s1)-1):
        tmp = ''.join(s1[i:i+2])
        if tmp.isalpha():
            a.append(tmp)
    for i in range(len(s2)-1):
        tmp = ''.join(s2[i:i+2])
        if tmp.isalpha():
            b.append(tmp)
    if len(a) == 0 and len(b) == 0:
        return 65536
    
    A = len(a)
    B = len(b)
    same= []
    for i in a:
        for j in b:
            if i== j:
                same.append(i)
                b.remove(i)
                break
    answer = len(same)/(A+B - len(same))
    answer = int(answer*65536)
            
    return answer
    