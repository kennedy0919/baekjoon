import sys
import heapq
# sys.stdin = open("input.txt", "r")

input = sys.stdin.readline

# graph = [[], [(2, 4), (3, 2), (4, 7)], [(1, 1), (3, 5)], [(1, 2), (4, 4)], [(2, 3)]]

def dijkstra(S, X):
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
        
    return distance[X]  

if __name__ == '__main__':
    N, M ,X = map(int, input().split())
    
    graph = [[] * (N + 1) for _ in range(0, N + 1)]
    ans = 0
    # INF = int(1e9)
    # distance = [INF] * (N + 1)
    
    for _ in range(0, M):
        s, e, m = map(int, input().split())
        graph[s].append((e, m))
    
    for i in range(1, N + 1):
        # graph = [[] * (N + 1) for _ in range(0, N + 1)]
        INF = int(1e9)
        distance = [INF] * (N + 1)  
        v_1 = dijkstra(i, X)
        
        distance = [INF] * (N + 1) 
        v_2 = dijkstra(X, i)
        
        ans_1 = v_1 + v_2
        
        if ans < ans_1 and X != i:
            ans = ans_1
            
    print(ans)