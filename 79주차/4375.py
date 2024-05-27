while True:
    try:
        n = int(input())
        if n == EOFError:
            break
        v = 1
        
        while True:
            if v % n == 0:
                print(len(str(v)))
                break
            v = (v*10)+1 # 문자열로 하면 계산 보다 더느려짐.
    except:
        break

    # 백준 배수.
    