def solution(a, b):
    answer = ''
    m = [0,31,29,31,30,31,30,31,31,30,31,30,31]
    day = (sum(m[:a]) + b) % 7
    d = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
    answer = d[day-3]
    return answer
# 2016년