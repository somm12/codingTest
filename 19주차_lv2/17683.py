def solution(m, musicinfos):
    answer = []
    high = ['C#','D#','F#','G#','A#']
    for i in high:
        m = m.replace(i,i[0].lower())
    
    for music in musicinfos:
        s,e,title,k = music.split(",")
        for i in high:
            k = k.replace(i,i[0].lower())
        s = list(map(int,s.split(":")))
        e = list(map(int,e.split(":")))
        time = (e[0] - s[0])*60 + (e[1]-s[1])
        total = ((time//len(k)) * k) + k[:time%len(k)]

        if m in total:
            answer.append((title,time))
    if len(answer) == 0:
        return '(None)'
    answer.sort(key = lambda x:-x[1])
    return answer[0][0]
# 방금 그곡