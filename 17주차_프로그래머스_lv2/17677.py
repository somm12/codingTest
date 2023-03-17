def solution(str1, str2):
    str1= str1.lower()
    str2 = str2.lower()
    len1 = len(str1)
    len2 = len(str2)
    same = []
    A = []
    for i in range(len1-1):
        a = str1[i:i+2]
        if a.isalpha():
            A.append(a)
    B = []
    for i in range(len2-1):
        b = str2[i:i+2]
        if b.isalpha():
            B.append(b)
    
    check = [0] * len(B)
    same = []
    tempB =[]
    for i in B:
        tempB.append(i)
    for i in A:
        if i in tempB:
            tempB.remove(i)
            same.append(i)
    if A == [] and B == []:
        return 65536
    else:
        s= len(same)
        a= len(A)
        b= len(B)
       
        return int((s/(a+b-s))*65536)
# 뉴스 클러스터링
# 교집합 구하기는 부분 유의하기