def solution(m, musicinfos):
    arr = ['C#','D#','F#','G#','A#']
    cand = []
    for v in arr:
        m = m.replace(v,v[0].lower())
    for v in musicinfos:
        s,e,title,info = v.split(",")
        st,sm = map(int, s.split(":"))
        et,em = map(int,e.split(":"))
        time = (et*60 + em) - (st*60+sm)
        for v in arr:
            info = info.replace(v,v[0].lower())
        total = info*(time//len(info)) + info[:(time%len(info))]
        if m in total:
            cand.append((title,time))
    if len(cand) == 0:
        return '(None)'
    cand.sort(key=lambda x: -x[1])
    return cand[0][0]
# 문자열 비교를 위해 #을 제거하기 위해서 replace 사용.
# 1. m에서 # 을 빼서 다른 문자로 대체
# 2. musicsinfo에서
    # 1. info 부분도 # 을 뺀다.
    # 2. 재생된 길이 구하고, 그만큼의 info 문자열 덩어리 구하기
    # 3. if m in info: 들었던 멜로디가 악보에 해당한다면
    # 4. cand.append((제목, 재생된 시간)) 후보 배열에 추가.
# 3. 만약 cand이 비었다면 None
# 4. 재생시간이 큰 기준으로 정렬
# 답 반환.

# 프로그래머스