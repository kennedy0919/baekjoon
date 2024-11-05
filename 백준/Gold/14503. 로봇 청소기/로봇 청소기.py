# import sys
# sys.stdin = open("input.txt", "r")

def dfs(r, c, D):
    global ans
    if arr[r][c] == 0:
        arr[r][c] = -1
        ans = ans + 1

    found_cleanable = False
    for _ in range(0, 4):
        if D == 0:
                D = 3
        else:
            D = D - 1

        nr = r + dr[D]
        nc = c + dc[D]

        if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0:
            dfs(nr, nc, D)
            found_cleanable = True
            break
            
            
    if not found_cleanable:
        nr = r - dr[D]
        nc = c - dc[D]
        if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] != 1:
            dfs(nr, nc, D)
        else:
            return


N ,M = map(int, input().split())
r, c, d = map(int, input().split()) # d = 0북 1동 2남 3서
arr = [list(map(int, input().split())) for _ in range(0, N)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

ans = 0
dfs(r, c, d)
print(ans)