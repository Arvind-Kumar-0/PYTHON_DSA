import collections
visited = False
def grapher(edges):
    graph = collections.defaultdict(list,[])
    for edge , backedge in edges:
        graph[edge].append([backedge,1])
        graph[backedge].append([edge,1])
    print(graph)
def shortest_path_from_src(graph,src):
    q = collections.deque([[src,0]])
    state = [not visited for _ in range(len(graph.keys()))]
    ans = [float('inf') for _ in range(len(graph.keys()))]
    while q:
        node , distance = q.popleft()
        
        ans[node] = min(ans[node],distance)
        if state[node] != visited:
            state[node] = visited
            for node , dx in graph[node]:
                q.append([node,distance+dx])
    return ans


graph = {
    0:[[1,1],[3,2]],
    1:[[6,1],[2,0],[0,1]],
    2:[[1,1],[4,3]],
    3:[[0,2],[5,10],[4,1]],
    4:[[2,3],[3,1]],
    5:[[3,10],[7,1]],
    6:[[1,1]],
    7:[[5,1]]
}
edges=[[0,1],[0,3],[3,4],[4,5],[5,6],[1,2],[2,6],[6,7],[7,8],[6,8]] 
grapher(edges=edges)
graph = collections.defaultdict(list,graph)
print(shortest_path_from_src(graph,0))
    
