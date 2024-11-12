# import sys
from collections import deque
# sys.stdin = open("input.txt", "r")

def bfs(r, c):
    q = deque([(0, 0, 0)])  
    v = [[[float('inf')] * 2 for _ in range(M)] for _ in range(N)]
    v[0][0][0] = 1  

    while q:
        r, c, wall_removed = q.popleft()
        if r == N - 1 and c == M - 1:
            return v[r][c][wall_removed]
        
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < M:
                if arr[nr][nc] == 0 and v[nr][nc][wall_removed] == float('inf'):
                    v[nr][nc][wall_removed] = v[r][c][wall_removed] + 1
                    q.append((nr, nc, wall_removed))
                
                if arr[nr][nc] == 1 and wall_removed == 0 and v[nr][nc][1] == float('inf'):
                    v[nr][nc][1] = v[r][c][wall_removed] + 1
                    q.append((nr, nc, 1))
    
    return -1

N, M = map(int, input().split())
arr = [list(input()) for _ in range(0, N)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
for r in range(0, N):
    for c in range(0, M):
        arr[r][c] = int(arr[r][c])

# ans = -1
# ans = bfs(0, 0)
# for r in range(0, N):
#     for c in range(0, M):
#         if arr[r][c] == 1:
#             arr[r][c] = 0
#             ans = max(ans, bfs(0, 0))
#             arr[r][c] = 1

ans = bfs(0, 0)
print(ans)
