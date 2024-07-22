# import sys
# sys.stdin = open("input.txt", "r")

from collections import deque

def bfs():
    global q
    global cnt
    ans = 0
    q = deque(q) 
    
    while q:
        r, c = q.popleft()  
        
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0:
                arr[nr][nc] = arr[r][c] + 1
                q.append((nr, nc))
                ans = max(ans, arr[nr][nc])
                cnt = cnt + 1
                       
    if cnt == N * M:
        print(ans - 1) 
        
    else:
        print(-1)
        

if __name__ == '__main__':

    M, N = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(0, N)]
    visited = [[0] * M for _ in range(0, N)]
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    q = []

    cnt = 0
    
    for i in range(0, N):
        for j in range(0, M):

            if arr[i][j] == -1:
                cnt = cnt + 1
                
            if arr[i][j] == 1:
                q.append((i, j))
                cnt = cnt + 1
    
    if cnt == N * M:
        print(0)
    
    else:
        bfs()
    