import sys
input = sys.stdin.readline



T = int(input())
for _ in range(T):
    x = list(input().strip())
    temp = list()
    ans = 1
    while len(x) > 0:
        while len(x) > 0  and x[-1] == ')':
            temp.append(x.pop())
        while len(x) > 0 and x[-1] == '(' and len(temp) > 0:
            x.pop()
            temp.pop()
        if (len(temp) == 0 and len(x) > 0 and  x[-1] == '(') or  (len(x) == 0 and len(temp) != 0):
            ans = 0
            break

    # print(x, temp)
    if ans == 1:
        print("YES")
    else:
        print("NO")
