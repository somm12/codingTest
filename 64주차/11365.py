while True:
    s = input()
    if s == 'END':
        break
    s = list(s)
    s.reverse()
    print(''.join(s))