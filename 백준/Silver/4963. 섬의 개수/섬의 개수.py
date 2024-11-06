# import sys
from collections import deque
# sys.stdin = open("input.txt", "r")


def bfs(r, c):
    q = deque()
    q.append((r, c))
    v[r][c] = 1

    while q:
        r, c = q.popleft()
        for d in range(0, 8):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < h and 0 <= nc < w and v[nr][nc] == 0 and arr[nr][nc] == 1:
                v[nr][nc] = 1
                q.append((nr, nc))
                # print("nr, nc :", nr, nc)
input_z = True

while (input_z == True):

    w, h = map(int, input().split())
    if w == 0 and h == 0:
        input_z = True
        break
    arr = [list(map(int, input().split())) for _ in range(0, h)]
    v = [[0] * w for _ in range(0, h)]
    dr = [-1, 0, 1, 0, -1, 1, 1, -1]
    dc = [0, 1, 0, -1, 1, 1, -1, -1]

    cnt = 0
    for r in range(0, h):
        for c in range(0, w):
            if arr[r][c] == 1 and v[r][c] == 0:
                # print("r, c :", r, c)
                bfs(r, c)
                # for i in v:
                    # print("i:", i)
                cnt = cnt + 1
                # print("##############")

    print(cnt)