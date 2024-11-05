# import sys
from collections import deque

# sys.stdin = open("input.txt", "r")

def combinations(virus, M): # M개 바이러스 선택 조합
    result = []

    def generate_combination(start, comb):
        if len(comb) == M:
            result.append(comb[:])
            return

        for i in range(start, len(virus)):
            comb.append(virus[i])
            generate_combination(i + 1, comb)
            comb.pop()
    
    generate_combination(0, [])
    return result

def bfs(comb):
    q = deque()
    v = [[-1] * N for _ in range(0, N)]
    for i in comb:
        r, c = i
        v[r][c] = 0
        q.append((r, c))
    max_time = 0

    while q:
        r, c = q.popleft()
        
        for d in range(0, 4):
            nr = r + dr[d]
            nc = c + dc[d]

            if 0 <= nr < N and 0 <= nc < N and v[nr][nc] == -1 and arr[nr][nc] != 1:
                v[nr][nc] = v[r][c] + 1
                q.append((nr, nc))
                if arr[nr][nc] == 0:
                    max_time = max(max_time, v[nr][nc])

    for r in range(0, N):
        for c in range(0, N):
            if arr[r][c] == 0 and v[r][c] == -1:
                return 10000
    
    return max_time


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(0, N)]
dr = [-1, 0, 1, 0]
dc = [0, 1 ,0 ,-1]
virus = []
for r in range(0, N):
    for c in range(0, N):
        if arr[r][c] == 2:
            virus.append((r, c))

comb = combinations(virus, M)
ans = 10000
for i in range(0, len(comb)):
    ans = min(ans, bfs(comb[i]))
    # print(ans)

if ans == 10000:
    ans = -1

print(ans)