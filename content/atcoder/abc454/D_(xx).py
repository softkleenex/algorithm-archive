import sys
input = sys.stdin.readline

t = int(input())

def change_xx(s):
    ans = list()
    for v in s:
        ans.append(v)
        if ans[-4:] == ['(', 'x', 'x', ')']:
            for _ in range(4):
                ans.pop()
            ans.extend("xx")
    return ans        
    
    
    
for _ in range(t):
    a = input().strip()
    a = change_xx(a)
    b = input().strip()
    b = change_xx(b)
    # print(*a, *b)
    if a == b:
        print("Yes")
    else:
        print("No")
    
