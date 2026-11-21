---
title: "[AtCoder] D_(xx)"
tags: ["AtCoder", "abc454"]
---

# D_(xx)

이 문제는 AtCoder에서 푼 문제입니다.
이 문제는 **abc454** 콘테스트 문제입니다.

🔗 [문제 바로가기](https://atcoder.jp/contests/abc454/tasks/abc454_d)


---

## 💡 해결 방법
<!-- 이 문제에 대한 접근 방식과 풀이를 작성하세요 -->
문자열 $a, b$ 각각에 대해 (xx) 패턴을 xx로 가능한 모든 구간에 대해 변환한 뒤, 두 문자열이 일치하는지 확인하는 방식으로 해결했습니다. 이때 string.replace()는 최악의 경우 $O(N^2)$의 시간 복잡도를 가져 시간 초과(TLE)가 발생할 수 있습니다. 따라서 **스택(Stack)**을 활용하여 문자열을 한 번만 순회($O(N)$)하면서 패턴을 감지하고 즉시 변환하는 효율적인 방식을 사용했습니다.

I solved this problem by transforming all occurrences of (xx) to xx in both strings a and b, then comparing the results. To aboid the O(N^2) time complexity overhead of string.replace(), which could lead to TLE, I implemeted an efficient O(N) approach using a stack to detect and replace the patterns in a single pass.

## 💻 코드

```python
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
    

```
