import sys
# sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(10000) 

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def dfs(r, c):
    
    arr[r][c] = 0
    
    for d in range(0, 4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 1:
            dfs(nr, nc)

            
            
T = int(input())

for tc in range(0, T):
    
    M, N, K = map(int, input().split())
    arr = [[0] * M for _ in range(0, N)]
    ans = 0
    
    for _ in range(0, K):
        s1, s2 = map(int, input().split())
        arr[s2][s1] = 1
    
    for i in range(0, N):
        for j in range(0, M):
            if arr[i][j] == 1:
                ans = ans + 1
                dfs(i, j)
    
    print(ans)
    
    
    