import sys
import heapq
# sys.stdin = open("input.txt", "r")

input = sys.stdin.readline

  
def dijkstra(K):
    q = []
    heapq.heappush(q, (0, K))
    distance[K] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        # print("dist, now", dist, now)
        
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]
            # print("i", i)
            # print("cost", cost)
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                # print(distance)
                heapq.heappush(q, (cost, i[0]))


if __name__ == '__main__':
    V, E = map(int, input().split())
    K = int(input())
    
    graph = [[] * (V + 1) for _ in range(0, V + 1)]
    INF = int(1e9)
    distance = [INF] * (V + 1)
    
    for _ in range(0, E):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
    
    dijkstra(K)
    for i in range(1, V + 1):
        if distance[i] == INF:
            print("INF")
        else:
            print(distance[i])