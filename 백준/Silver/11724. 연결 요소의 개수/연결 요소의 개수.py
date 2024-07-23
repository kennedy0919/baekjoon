# import sys
# sys.stdin = open("input.txt", "r")

from collections import deque
import sys
input = sys.stdin.readline


def bfs(i):
    global q
    global visited
    q = deque(q)

    q.append(i)
    visited[i] = 1
    
    while q:
        c = q.popleft()
        for i in adj[c]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1

N, M = map(int, input().split())

adj = [[] for _ in range(0, N + 1)]

for _ in range(0, M):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)
    
cnt = 0
q = []
visited = [0] * (N + 1)

for i in range(1, N + 1):
    if visited[i] == 0:
        bfs(i)
        cnt = cnt + 1

print(cnt)