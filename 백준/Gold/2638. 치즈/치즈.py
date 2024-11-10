# import sys
from collections import deque
# sys.stdin = open("input.txt", "r")

def melt_cheeze(r, c):
    q = deque()
    v = [[0] * M for _ in range(0, N)]
    q.append((r, c))
    v[r][c] = 1
    melt = []

    while q:
        r, c = q.popleft()
        for d in range(0, 4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < M:
                if arr[nr][nc] == 0 and v[nr][nc] == 0:
                    q.append((nr, nc))
                    v[nr][nc] = 1
                    # for i in v:
                    #     print(i)
                    # print("#######################")
                if arr[nr][nc] == 1 and v[nr][nc] == 0:
                    melt_cnt = 0
                    for k in range(0, 4):
                        nx = nr + dr[k]
                        ny = nc + dc[k]
                        if 0 <= nx < N and 0 <= ny < M:
                            if arr[nx][ny] == 0 and v[nx][ny] == 1:
                                melt_cnt = melt_cnt + 1
                    if melt_cnt >= 2:
                        melt.append((nr, nc))
                        v[nr][nc] = 1
                    
    for r, c in melt:
        arr[r][c] = 0


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(0, N)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

time = 0
while True:
    # print("#1")
    # for i in arr:
    #     print(i)
    # print("##################")
    cnt = 0
    for r in range(0, N):
        for c in range(0, M):
            if arr[r][c] == 1:
                cnt = cnt + 1
    if cnt == 0:
        print(time)
        break
    melt_cheeze(0, 0)
    time = time + 1