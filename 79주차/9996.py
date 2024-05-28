n = int(input())
p = input()
front, rear = p.split("*")
while n > 0:
    s = input()
    if len(p) - 1 > len(s):# 별빼고 모든 문자수의 패턴이 더 많다면 NE.
        print("NE")
    else:
        a,b = s[:len(front)],s[len(s)- len(rear):]# 별을 기준으로, 앞 뒤 부분의 문자개수 만큼 입력받은 s도 같은 문자수 만큼 잘라서 확인.
        
        if a == front and b == rear :# 같으면 DA
            print("DA")
        else:
            print("NE")
    
    n -= 1
# 백준 한국이 그리울 땐 서버에 접속하지