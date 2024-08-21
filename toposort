def dfs(node):
    if node in visited:
        return
    visited.add(node)
    for neighbor , weight in graph.get(node):
        if neighbor not in visited:
            dfs(neighbor)
    stack.append(node)
#remove the weight to toposort dfs in unweighted graph


###bfs
