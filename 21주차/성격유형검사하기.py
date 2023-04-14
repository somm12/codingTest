def solution(survey,choices):
    answer = ''
    a = {'R':0, 'T':0}
    b = {'C': 0, 'F':0}
    c = {'J':0, 'M':0}
    d = {'A':0, 'N':0}
    
    for i,v in enumerate(survey):
        l = v[0]
        r = v[1]
        if l in d:
            if choices[i] > 4:
                d[r] += abs(choices[i] - 4)
            else:
                d[l] += abs(choices[i] - 4)
        elif l in a:
            if choices[i] > 4:
                a[r] += abs(choices[i] - 4)
            else:
                a[l] += abs(choices[i] - 4)
        elif l in b:
            if choices[i] > 4:
                b[r] += abs(choices[i] - 4)
            else:
                b[l] += abs(choices[i] - 4)
        elif l in c:
            if choices[i] > 4:
                c[r] += abs(choices[i] - 4)
            else:
                c[l] += abs(choices[i] - 4)
    a= list(a.items())
    a.sort(key=lambda x:(-x[1],x[0]))
    
    b= list(b.items())
    b.sort(key=lambda x:(-x[1],x[0]))
    
    c= list(c.items())
    c.sort(key=lambda x:(-x[1],x[0]))
    
    d= list(d.items())
    d.sort(key=lambda x:(-x[1],x[0]))
    
    return a[0][0] + b[0][0] + c[0][0] + d[0][0]