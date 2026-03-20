from collections import defaultdict, deque
def solution(n, edge):
    # node : n
    # starts: 1
    INF = 50001
    graph = defaultdict(list)
    graph[0] = []
    visited = set()
    dist = [INF for _ in range(n+1)]
    dist[1] = 0 # start point
    
    for src, dst in edge:
        graph[src].append(dst)
        graph[dst].append(src)
        
    q = deque()
    q.append(1)
    
    far = 0
    while q:
        cur = q.popleft()
        for node in graph[cur]:
            if node in visited:
                continue
            if dist[cur] + 1 < dist[node]: # 최단거리 갱신
                dist[node] = dist[cur] + 1
                far = max(far, dist[node])
                q.append(node)
        visited.add(cur)
        
    cnt = len([d for d in dist[1:] if d == far])
        
    return cnt

# test case
tc = {
    1: (6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]), # 3
}
print(solution(tc[1][0], tc[1][1]))
