from itertools import permutations
from collections import deque
def calc(a,op,b):
    if op == '*':
        return a*b
    elif op == '-':
        return a-b
    elif op == '+':
        return a+b
def solution(expression):
    answer =0
    tmp = ''
    arr =[]
    for i in expression:
        if i.isdecimal():
            tmp += i
        else:
            arr.append(int(tmp))
            arr.append(i)
            tmp = ''
    arr.append(int(tmp))
    
    arr = deque(arr)
    op = ['*','+','-']
    for ops in list(permutations(op,3)):
        a = deque(arr.copy())
        for o in ops:
            stack = []
            while a:
                x = a.popleft()
                if x != o:
                    stack.append(x)
                else:
                    left = stack.pop()
                    right = a.popleft()
                    result = calc(left,o,right)
                    
                    stack.append(result)
            a = deque(stack)   
            
        answer =max(abs(a[0]),answer)    
    return answer