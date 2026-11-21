

a = []
b = []
n = int(input())
for _ in range(n):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)


m = int(input())

bones = list()
for _ in range(m):
    s = input()
    bones.append(s)


ribs_features = set()
for v in bones:
    L = len(v)
    for j in range(L):
        ribs_features.add((v[j], L, j))



def select_ribs(x, a , b):#bones에서 길이가 a이고 x의 b번째 문자와 같은 b번쨰 문자가 같은  bones를 return한다.
    global bones
    complete_bones = []
    if (x, a, b) in ribs_features:
        return [True]
    return []


for spine in bones:
    if len(spine) != n:
        print("No")
        continue


    for i in range(n):
        if len(select_ribs(spine[i] , a[i] , b[i] - 1)) == 0:
            print("No")
            break
    else:
        print("Yes")


