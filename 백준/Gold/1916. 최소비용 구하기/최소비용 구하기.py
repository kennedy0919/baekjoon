import sys
import heapq
# sys.stdin = open("input.txt", "r")

input = sys.stdin.readline


def dijkstra(S, E):
    q = []
    heapq.heappush(q, (0, S))
    distance[S] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]
            
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return distance[E]
    
if __name__ == '__main__':
    N = int(input())
    M = int(input())
    
    graph = [[] * (N + 1) for _ in range(0, N + 1)]
    INF = int(1e9)
    distance = [INF] * (N + 1)
    
    for _ in range(0, M):
        s, e, m = map(int, input().split())
        graph[s].append((e, m))
    
    S, E = map(int, input().split())
    
    ans = dijkstra(S, E)
    
    print(ans)
    