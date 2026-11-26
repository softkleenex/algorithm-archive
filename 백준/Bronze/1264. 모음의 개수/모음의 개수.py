while 1:
    x = list(input())
    if x == ['#']:
        break
    ans = 0
    for v in x:

        if v == 'a' or v == 'e' or v == 'i' or v == 'o' or v == 'u' or v == 'A' or v == 'E' or v == 'I' or v == 'O' or v == 'U':
            ans += 1
    print(ans)
