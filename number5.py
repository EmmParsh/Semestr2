def DFS(curr_node, adj_list, visited=None):
    if visited is None:
        visited = set()
    print("Enter:", curr_node)
    visited.add(curr_node)
    for adj_node in adj_list[curr_node]:
        if adj_node not in visited:
            DFS(adj_node, adj_list, visited)
    print("Exit:", curr_node)
    return visited

n = int(input())
graph = {}
for i in range(n):
    row = input()
    next_heads = [int(i) for i in row.split()]
    graph[i] = next_heads

print("DFS traveler:")
DFS(0, graph)