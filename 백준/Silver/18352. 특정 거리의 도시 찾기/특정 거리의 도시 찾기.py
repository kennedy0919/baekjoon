import sys
import heapq
# sys.stdin = open("input.txt", "r")

input = sys.stdin.readline

def dijkstra(X):
    q = []
    heapq.heappush(q, (0, X))
    distance[X] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]
            
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    
    return distance


if __name__ == '__main__':
    N, M, K, X = map(int, input().split())
    
    graph = [[] for _ in range(0, N + 1)]
    INF = int(1e9)
    distance = [INF] * (N + 1)
    
    for i in range(0, M):
        A, B = map(int, input().split())
        graph[A].append((B, 1))
    
    G = dijkstra(X)
    
    cnt = 0
    for i in range(0, N + 1):
        if G[i] == K:
            cnt = cnt + 1
            print(i)
    
    if cnt == 0:
        print("-1")