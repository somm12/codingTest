def solution(today, terms, privacies):
    answer = []
    dict = {}
    for i in terms:
        a,b = i.split()
        dict[a] = int(b)
    y,m,d = map(int,today.split("."))
    today = y*12*28 + m*28 + d
    
    for i,v in enumerate(privacies):
        v = v.replace(" ",".")
        y,m,d,k = v.split(".")
        tmp = int(y)*12*28 + int(m)*28 + int(d) + dict[k]*28
        if today >= tmp:
            answer.append(i+1)
    return answer