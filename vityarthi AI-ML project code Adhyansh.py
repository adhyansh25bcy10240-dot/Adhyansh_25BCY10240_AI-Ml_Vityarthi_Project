graph = {'A': ['C', 'B', 'D'], 'B': ['E'], 'C': ['E', 'D'], 'D': [], 'E': []}

visited_nodes = set()

def traverse_root(visited_nodes, graph, root):
    if root not in visited_nodes:
        print("Visiting:", root)
        visited_nodes.add(root)

        count = 1  

        for next in graph[root]:
            count =count+traverse_root(visited_nodes, graph, next)

        return count
    
    return 0  

total = traverse_root(visited_nodes, graph, 'A')
print("Total nodes visited:", total)


