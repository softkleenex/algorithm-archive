while 1:
    x = list(input())
    if x == ['0']:
        break
    # print(x)
    ans = 2
    for v in x:
        if v == '0':
            ans += 4
        elif v == '1':
            ans += 2
        else:
            ans += 3
    ans += 1 * (len(x) - 1)
    print(ans)
