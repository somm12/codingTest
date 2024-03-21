import math
def check(num,start,end):
    root = (start+end)//2
    left = (start+(root-1))//2
    right = (root+1+end)//2
    if (start==end):# 부모가 0인데, 자식이 1이라면 표현할수 없는 이진트리.
        return True
    if (num[root] == '0'and( num[left]=='1'or num[right]=='1')):
        return False
    return check(num,start,root-1) and check(num,root+1,end)
    
def solution(numbers):
    answer = []
    for v in numbers:
        binNum = bin(v)[2:]
        h = int(math.log2(len(binNum)))+1
        totalLen = (2**h)-1
        binNum = '0'*(totalLen - len(binNum)) + binNum
        if check(binNum,0,totalLen-1):
            answer.append(1)
        else:
            answer.append(0)
    return answer