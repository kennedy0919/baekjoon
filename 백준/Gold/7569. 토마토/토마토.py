# import sys
# sys.stdin = open("input.txt", "r")

from collections import deque

# [0, -1, 3, 2, 2]
# [-1, -1, 2, 1, 1]
# [4, 3, 2, 1, 1]

def bfs(tomato, empty):
    q = deque()

    for r, c, h in tomato:
        visited[h][r][c] = 1
        q.append((r, c, h))
    
    for r, c, h in empty:
        visited[h][r][c] = 1
    
    while q:
        r, c, h = q.popleft()
        for d in range(0, 6):
            nr = r + dr[d]
            nc = c + dc[d]
            nh = h + dh[d]
            if 0 <= nr < N and 0 <= nc < M and 0<= nh < H and visited[nh][nr][nc] == 0 and arr[nh][nr][nc] == 0:
                visited[nh][nr][nc] = 1
                arr[nh][nr][nc] = arr[h][r][c] + 1
                q.append((nr, nc, nh))

    return arr
    

M, N, H = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

tomato = []
empty = []
for h in range(H):
    for r in range(N):
        for c in range(M):
            if arr[h][r][c] == 1:
                tomato.append((r, c, h))
            if arr[h][r][c] == -1:
                empty.append((r, c, h))

q = []
cnt = 0
ans = 0
visited = [[[0] * M for _ in range(0, N)] for _ in range(0, H)]
# 상, 하, 좌, 우, 위, 아래를 포함한 3차원 방향 배열
dr = [1, -1, 0, 0, 0, 0]  # 행 이동 (위/아래)
dc = [0, 0, 1, -1, 0, 0]  # 열 이동 (좌/우)
dh = [0, 0, 0, 0, 1, -1]  # 높이 이동 (위/아래)
# print("tomato", tomato)
# print("empty", empty)

bfs_arr = bfs(tomato, empty)

for h in range(H):
    for r in range(N):
        for c in range(M):
            if bfs_arr[h][r][c] != 0:
                cnt = bfs_arr[h][r][c]
            if ans < cnt:
                ans = cnt
                
ans = ans - 1         
# print("#1 ans", ans)

for h in range(H):
    for r in range(N):
        for c in range(M):
            if bfs_arr[h][r][c] == 0:
                ans = -1
                
# print("#2 ans", ans)



# for h in range(0, H):
#     for i in range(0, N):
#         print(arr[h][i])
    
# ans = bfs(tomato, empty)
print(ans)
# print(ans)