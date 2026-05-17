---
title: "[AtCoder] C_Fishbones"
tags: ["AtCoder", "abc452"]
---

# C_Fishbones

이 문제는 AtCoder에서 푼 문제입니다.
이 문제는 **abc452** 콘테스트 문제입니다.

🔗 [문제 바로가기](https://atcoder.jp/contests/abc452/tasks/abc452_c)


---

## 💡 해결 방법
<!-- 이 문제에 대한 접근 방식과 풀이를 작성하세요 -->
AT는 물고기 뼈 모양의 오브제를 만들었는데, 1~N까지의 글자가 매겨진 N개의 갈비뼈 하나와 척추 하나로 구성되어있다.
N+1개의 뼈 각각에 문자열을 쓰자.
척추에 적힌 문자열의 길이는 N이다.
갈비뼈 i = 1,...,N에 적힌 문자열은,
    갈비뼈 i에 적힌 문자열의 길이는 A_i이다.
    갈비뼈 i에 적힌 문자열의 B_i번쨰 문자는 척추의 i번쨰 글자와 같다.

S_1,...,S_m 문자열은 모두 영어 소문자로 이루어진 서로 다른 문자열이다.(중복은 허용)

막약 척추에 Sj라는 문자열을 적는다면, 위의 조건들을 모두 만족하도록 나머지 N개의 갈비뼈를 구성할 수 있는가?

문제 이해해 오랜 시간이 걸렸다. 한글로 한번 적어도 잘 이해가 가지않아, gemini 의 도움을 받았다. 처음보는 구조의 문제라 그랬던것 같다.
조건을 만족하는 bone이 있는지 유무를 빠르게 판단하는것이 중요하기 때문에, set을 사용하여 문제를 해결햐였다.


## 💻 코드

```python


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



```
