from itertools import permutations
from collections import deque
def cal(x,y,op):
    
    if op == '*':
        return str(int(x) * int(y))
    elif op == '-':
        return str(int(x) - int(y))
    elif op == '+':
        return str(int(x) + int(y))

def solution(ex):
    answer = 0
    a = ''
    arr= []
    for i in ex:
        if i.isdecimal():
            a+= i
        else:
            arr.append(a)
            arr.append(i)
            a = ''
    arr.append(a)
    dict = {}
    for i in ex:
        if not i.isdecimal():
            if i not in dict:
                dict[i]= 1
    dict = list(dict.keys())
    
    
    for i in list(permutations(dict,len(dict))):
        ex = arr.copy()
        for op in i:
            new = []
            while len(ex) != 0:
                x = ex.pop(0)
                if x == op and ex:
                    new.append(cal(new.pop(), ex.pop(0),op))
                else:
                    new.append(x)
            ex = new
            if len(ex) == 1:
                answer = max(answer,abs(int(ex[0])))
         
    return answer
# 수식 최대화