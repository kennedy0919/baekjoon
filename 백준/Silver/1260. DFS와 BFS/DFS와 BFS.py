# import sys
# sys.stdin = open("input.txt", "r")


def dfs(c):
    v[c] = 1
    ans_dfs.append(c)
    for n in adj[c]:
        if v[n] == 0:
            dfs(n)
    

def bfs(s):
    q = []
    q.append(s)
    ans_bfs.append(s)
    v[s] = 1
    
    while q:
        c = q.pop(0)
        for n in adj[c]:
            if v[n] == 0:
                q.append(n)
                ans_bfs.append(n)
                v[n] = 1
            


N, M, V = map(int, input().split())
adj = [[] for _ in range(0, N + 1)]

for _ in range(0, M):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)
    
# print(adj)

for i in range(1, N + 1):
    adj[i].sort()
    
# print(adj)
v = [0] * (N + 1)
ans_dfs = []
dfs(V)

v = [0] * (N + 1)
ans_bfs = []
bfs(V)

print(*ans_dfs)
print(*ans_bfs)