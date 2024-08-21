def detect_cycle(graph):
    
    WHITE, GREY, BLACK = 0, 1, 2  
    color = {node: WHITE for node in graph}  
    
    def dfs(node):
        if color[node] == GREY:
            return True  
        if color[node] == BLACK:
            return False  
        color[node] = GREY  
        for neighbor in graph[node]:
            if dfs(neighbor):
                return True  
        color[node] = BLACK  
        return False
    for node in graph:
        if color[node] == WHITE:
            if dfs(node):
                return True      
    return False
