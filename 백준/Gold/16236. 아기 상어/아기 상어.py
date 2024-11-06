# import sys
from collections import deque

# sys.stdin = open("input.txt", "r")

def bfs(r, c):
    shark = 2
    shark_cnt = 0
    sec = 0

    while True:
        q = deque()
        v = [[-1] * N for _ in range(N)]
        q.append((r, c))
        v[r][c] = 0
        fish_list = []

        while q:
            len_q = len(q)
            for _ in range(0, len_q):
                r, c = q.popleft()
                dist = v[r][c]

                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]
                    if 0 <= nr < N and 0 <= nc < N and v[nr][nc] == -1:
                        if arr[nr][nc] <= shark:
                            v[nr][nc] = dist + 1
                            q.append((nr, nc))
                            if 0 < arr[nr][nc] < shark:
                                fish_list.append((dist + 1, nr, nc))
            
                if fish_list:
                    break

        if len(fish_list) > 0:
            fish_list.sort()
            dist, r, c = fish_list[0]
            sec = sec + dist
            shark_cnt = shark_cnt + 1
            if shark_cnt == shark:
                shark = shark + 1
                shark_cnt = 0
            arr[r][c] = 0
            # for i in arr:
            #     print(i)
            # print("########################")
            
        else:
            return sec

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

for r in range(N):
    for c in range(N):
        if arr[r][c] == 9:
            arr[r][c] = 0
            start_r, start_c = r, c

print(bfs(start_r, start_c))
