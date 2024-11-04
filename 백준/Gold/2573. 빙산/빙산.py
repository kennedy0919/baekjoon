# import sys
from collections import deque

# sys.stdin = open("input.txt", "r")

def bfs(r, c, visited):
    q = deque()
    q.append((r, c))
    visited[r][c] = 1

    while q:
        r, c = q.popleft()
        for d in range(0, 4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc <= M and visited[nr][nc] == 0 and arr[nr][nc] > 0:
                q.append((nr, nc))
                visited[nr][nc] = 1


def solve():  
    for year in range(1, 900000):
        v = [[0] * M for _ in range(0, N)]
        for r in range(0, N):
            for c in range(0, M):
                if arr[r][c] == 0:
                    continue
                for d in range(0, 4):
                    nr = r + dr[d]
                    nc = c + dc[d]
                    if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0:
                        v[r][c] = v[r][c] + 1

        for r in range(0, N):
            for c in range(0, M):
                if v[r][c] > 0:
                    arr[r][c] = max(0, arr[r][c] - v[r][c])

        visited = [[0] * M for _ in range(0, N)]
        cnt = 0
        for r in range(0, N):
            for c in range(0, M):
                if visited[r][c] == 0 and arr[r][c] > 0:
                    bfs(r, c, visited)
                    cnt = cnt + 1
                    if cnt > 1:
                        return year

        if cnt == 0:
            return 0


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(0, N)]
dr = [-1, 0, 1, 0]
dc = [0, 1 ,0, -1]

ans = solve()

print(ans)

