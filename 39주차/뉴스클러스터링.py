from collections import defaultdict
def solution(str1,str2):
    answer = 0
    a = []
    b = []
    same = []
    union = []
    dict1 = defaultdict(int)
    dict2 = defaultdict(int)
    str1 = str1.lower()
    str2= str2.lower()
    
    for i in range(len(str1)-1): # 두 글자씩 끊어서 배열에 넣기.
        tmp = str1[i:i+2]
        if tmp.isalpha():
            a.append(tmp)
    for i in range(len(str2)-1):# 두 글자씩 끊어서 배열에 넣기.
        tmp = str2[i:i+2]
        if tmp.isalpha():
            b.append(tmp)
    
    for v in a: # 각 문자열이 몇 개인지 dictionary에 할당.
        dict1[v] += 1
    for v in b:
        dict2[v] += 1

    for s in a: # 같은 부분이 있으면 -1, 교집합에 추가.
        if s in dict2 and dict2[s] > 0:
            
            dict1[s] -= 1
            dict2[s] -= 1
            same.append(s)
    
    for s in dict1:# dict1에 남은 문자열은 합집합에 추가
        if dict1[s] > 0 :
            for _ in range(dict1[s]):
                union.append(s)
    
    for s in dict2:# dict2에 남은 문자열은 합집합에 추가
        if dict2[s] > 0 :
            for _ in range(dict2[s]):
                union.append(s)
    
    union += same # 교집합 마저 추가.
    
    if len(union) == 0 and len(same) == 0:# 공집합이라면 유사도는 1
        return 65536
    
    
    return int((len(same)/len(union))*65536)
# 프로그래머스 카카오문제