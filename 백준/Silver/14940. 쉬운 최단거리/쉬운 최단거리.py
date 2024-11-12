# import sys
from collections import deque
# sys.stdin = open("input.txt", "r")

def bfs(r, c):
    q = deque()
    v = [[float('inf')] * M for _ in range(0, N)]
    q.append((r, c))
    v[r][c] = 0

    while q:
        r, c = q.popleft()
        for d in range(0, 4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < M and v[nr][nc] == float('inf'):
                if arr[nr][nc] == 1:
                    q.append((nr, nc))
                    v[nr][nc] = v[r][c] + 1
                
    
    for r in range(0, N):
        for c in range(0, M):
            if arr[r][c] == 0:
                v[r][c] = 0
            if v[r][c] == float('inf'):
                v[r][c] = -1

    return v

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(0, N)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
for r in range(0, N):
    for c in range(0, M):
        if arr[r][c] == 2:
            ans_arr = bfs(r, c)

for r in range(0, N):
    cnt = 0
    for c in range(0, M):
        cnt = cnt + 1
        if r == N - 1 and c == M - 1:
            print(ans_arr[r][c])
            break
        if cnt == M:
            print(ans_arr[r][c])
        else:
            print(ans_arr[r][c], end = " ")
