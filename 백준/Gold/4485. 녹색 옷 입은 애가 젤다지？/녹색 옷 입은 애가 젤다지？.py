import sys
import heapq
# sys.stdin = open("input.txt", "r")

input = sys.stdin.readline

n = int(input())
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

cnt = 0

while n != 0:
    cnt += 1
    board = [list(map(int, input().split())) for _ in range(n)]
    heap = []
    dist = [[1e9] * n for _ in range(n)]
    
    dist[0][0] = board[0][0]
    heapq.heappush(heap, (board[0][0], 0, 0))

    while heap:
        distance, c, r = heapq.heappop(heap)

		
        if c == n-1 and r == n-1:
            print("Problem", str(cnt)+":", distance)
            
            n = int(input())
            break
		
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
			
            if 0 <= nc < n and 0 <= nr < n:
                cost = distance + board[nc][nr]
                
                if dist[nc][nr] > cost:
                    dist[nc][nr] = distance + board[nc][nr]
                    heapq.heappush(heap, (distance + board[nc][nr], nc, nr))