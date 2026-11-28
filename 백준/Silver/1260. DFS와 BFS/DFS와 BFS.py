
from collections import deque

def dfs(graph, start):
    visited = {i : False for i in graph.keys()}
    stack = [start]
    order = []

    while stack:
        current = stack.pop()

        if visited[current]:
            continue
        visited[current] = True
        order.append(current)
        for nxt in sorted(graph[current], reverse = True):
            if not visited[nxt]:
                stack.append(nxt)
    print(*order)

def bfs(graph, start):
    visited = {i : False for i in graph.keys()}
    queue = deque([start])
    visited[start]= True
    order = []
    while queue:
        current = queue.popleft()
        order.append(current)
        for nxt in sorted(graph[current]):
            if not visited[nxt]:
                queue.append(nxt)
                visited[nxt] = True
    print(*order)


N, M, V = map(int, input().split())
graph = dict()
for i in range(1, N+1):
    graph[i] = []


for v in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


dfs(graph, V)
bfs(graph, V)
