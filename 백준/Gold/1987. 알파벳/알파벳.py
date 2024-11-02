# import sys
from collections import deque
# sys.stdin = open("input.txt", "r")

# ['H', 'F', 'D', 'F', 'F', 'B']
# ['A', 'J', 'H', 'G', 'D', 'H']
# ['D', 'G', 'A', 'G', 'E', 'H']

def bfs(a, b):
    global ans

    q = deque()
    visited[a][b].add(board[a][b])    
    q.append((a, b, board[a][b]))

    while q:
        r, c, pq = q.popleft()
        # print(pq)
        ans = max(ans, len(pq))
        for d in range(0, 4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < R and 0 <= nc < C and board[nr][nc] not in pq:
                if pq + board[nr][nc] not in visited[nr][nc]:
                    q.append((nr, nc, pq + board[nr][nc]))
                    visited[nr][nc].add((pq + board[nr][nc]))
                
    return ans
                 

R, C = map(int, input().split())
board = [list(input()) for _ in range(0, R)]

visited = [[set() for _ in range(0, C)] for _ in range(0, R)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
ans = 1

bfs(0, 0)

print(ans)
