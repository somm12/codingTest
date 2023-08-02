def solution(plans):
    answer = []
    new =[]
    for name,start,play in plans:
        h,m = map(int,start.split(":"))
        new.append((name,h*60+m, int(play)))
    plans = new
    plans.sort(key=lambda x:x[1])
    lefttime = 0
    stack = []
    for i in range(len(plans)):
        name,start,play = plans[i]
        while stack:
            nam,playtime = stack.pop()
            if lefttime >= playtime:
                answer.append(nam)
                lefttime -= playtime
            else:
                stack.append((nam, playtime-lefttime))
                break
        stack.append((name,play))
  
        if i < len(plans)-1:
            lefttime= plans[i+1][1] - start
    
    while stack:
        answer.append(stack.pop()[0])
    return answer
# 프로그래머스 lv2