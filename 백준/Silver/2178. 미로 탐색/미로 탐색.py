# import sys
# sys.stdin = open("input.txt", "r")

def bfs(sr, sc, er, ec):
    q = []
    visited = [[0] * M for _ in range(0, N)]
    
    q.append((sr, sc))
    visited[sr][sc] = 1
    
    while q:
        r, c = q.pop(0)
        
        if (r, c) == (er, ec):
            return visited[er][ec]
        
        
        for d in range(0, 4):
            nr = r + dr[d]
            nc = c + dc[d]
    
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 1 and visited[nr][nc] == 0: 
                q.append((nr, nc))
                visited[nr][nc] = visited[r][c] + 1
                

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(0, N)]
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

ans = bfs(0, 0, N - 1, M - 1)
print(ans)