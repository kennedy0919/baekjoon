import sys
import heapq

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

# graph = [[], [(2, 3), (3, 5), (4, 4)], [(3, 3), (4, 5)], [(4, 1)], []]

def dijkstra(S, E):
    q = []
    distance = [INF] * (N + 1)
    
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
    
        
    # print("distance[E]:", distance)
    return distance[E]


if __name__ == '__main__':
    N, E = map(int, input().split())
    
    graph = [[] for _ in range(0, N + 1)]
    INF = int(1e9)
    
    for _ in range(0, E):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
    
    v1, v2 = map(int, input().split())
    
    ans_1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N)
    ans_2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, N)
    
    # print("1, 2:", ans_1, ans_2)
    
    if ans_1 < ans_2:
        ans = ans_1
    
    else:
        ans = ans_2
    
    if ans_1 >= INF and ans_2 >= INF:
        ans = -1
    
    print(ans)