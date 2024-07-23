# import sys
# sys.stdin = open("input.txt", "r")

from collections import deque

def bfs(X, K):
    global q
    global cnt
    q = deque(q)
    visited = [0] * 100001
    visited[X] = 1
    q.append((X, 0))

    while q: 
        X, cnt = q.popleft()
        if X == K:
            return cnt
        
        for next_p in (X * 2, X + 1, X - 1):
            if 0 <= next_p < 100001 and not visited[next_p]:
                visited[next_p] = 1
                q.append((next_p, cnt + 1))
    
    
if __name__ == '__main__':
    
    N, K = map(int, input().split())
    q = []
    cnt = 0
    visited = [0] * 100000
    
    ans = bfs(N, K)
    print(ans)
    
    