
def solution(files):
    answer = []
    arr = [] # [(HEAD 부분 소문자, NUMBER 부분, 원래 문자)] 형식으로 담을 배열.
    for file in files:
        head = ''
        num = ''
        for i in range(len(file)): # 숫자가 아닌 부분 모든 문자까지 head에 추가.
            if not file[i].isdigit():
                head += file[i]
            else: 
                last = i # 숫자가 나오면 해당 idx 저장.
                break
        for i in range(last, len(file)): # 숫자 부분 num에 추가
            if file[i].isdigit():
                num += file[i]
            else:
                break
        
        arr.append((head.lower(), int(num), file)) # HEAD기준 > 문자열 기준이 아닌 숫자형식 기준 정렬. 순으로 정렬. ** 이 때 대소문자 구분이 없다는 것에 주의해서 lower() 사용.
    arr.sort(key=lambda x:(x[0],x[1]))
    answer = [v[2] for v in arr]
    return answer
# 프로그래머스 카카오 문제 
