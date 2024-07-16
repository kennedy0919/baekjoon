# import sys
# sys.stdin = open("input.txt", "r")

def dfs(c):
    visited[c] = 1
    # print(visited)
    for i in adj[c]:
        if visited[i] == 0:
            dfs(i)



N = int(input())
M = int(input())

adj = [[] for _ in range(0, N + 1)]
visited = [0] * (N + 1)

for _ in range(0, M):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)

# print(adj)
ans = -1

dfs(1)

for i in visited:
    if i == 1:
        ans = ans + 1
print(ans)