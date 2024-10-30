# import sys

# sys.stdin = open("input.txt", "r")

from collections import deque

def bfs(tlst):
    for i,j in tlst:
        arr[i][j] = 1
    
    
    q = deque()
    V2 = [[0] * M for _ in range(0, N)]
    count = cnt - 3   # 남은 0의 개수
        
    for ti, tj in virus:
        q.append((ti, tj))
        V2[ti][tj] = 1
        
    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj+ dj
            if 0 <= ni < N and 0 <= nj < M and V2[ni][nj] == 0 and arr[ni][nj] == 0:
                q.append((ni, nj))
                V2[ni][nj] = 1
                count = count - 1
    for i,j in tlst:
        arr[i][j] = 0
    return count     
    
    
def dfs(n, tlst):
    global ans
    if n == 3:
        ans = max(ans, bfs(tlst))
        return
    
    for j in range(0, cnt):
        if V[j] == 0:
            V[j] = 1
            dfs(n + 1, tlst + [lst[j]])
            V[j] = 0
    
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(0, N)]

lst = []
virus = []
for i in range(0, N):
    for j in range(0, M):
        if arr[i][j] == 0:
            lst.append((i, j))
        elif arr[i][j] == 2:
            virus.append((i, j))
            
cnt = len(lst)
V = [0] * cnt
ans = 0

dfs(0, [])

print(ans)    
    
