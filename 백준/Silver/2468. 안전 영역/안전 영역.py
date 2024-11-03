# import sys
from collections import deque
# sys.stdin = open("input.txt", "r")

# [6, 8, 2, 6, 2]
# [3, 2, 3, 4, 6]
# [6, 7, 3, 3, 2]
# [7, 2, 5, 3, 6]
# [8, 9, 5, 2, 7]

def bfs(sr, sc, h):
    q = deque()
    q.append((sr, sc))
    v[sr][sc] = 1

    while q:
        r, c = q.popleft()
        for d in range(0, 4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < N and v[nr][nc] == 0 and arr[nr][nc] > h:
                q.append((nr, nc))
                v[nr][nc] = 1
    

def solve(h):
    cnt = 0
    for r in range(0, N):
        for c in range(0, N):
            if v[r][c] == 0 and arr[r][c] > h:
                bfs(r, c, h)
                cnt = cnt + 1
    return cnt



N = int(input())
arr = [list(map(int, input().split())) for _ in range(0, N)]
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

max_num = 0
for r in range(0, N):
    for c in range(0, N):
        if max_num < arr[r][c]:
            max_num = arr[r][c]

ans = 0
for i in range(0, max_num):
    v = [[0] * N for _ in range(0, N)]
    ans = max(ans, solve(i))

print(ans)
