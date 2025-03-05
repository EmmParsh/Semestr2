def BFS(start_node, adj_list, visited=None):
    queue = [(start_node, 0)]
    if visited is None:
        visited = set()
    while len(queue) > 0:
        curr_node, dist = queue.pop(0)
        visited.add(curr_node)
        for adj_node in adj_list[curr_node]:
            if adj_node not in visited:
                queue.append((adj_node, dist + 1))
    return visited

def count_components(adj_list):
    visited = set()
    count = 0
    for node in range(len(adj_list)):
        if node not in visited:
            BFS(node, adj_list, visited)
            count += 1

    return count

n = int(input())
adj_list = []
for i in range(n):
    row = input()
    next_heads = [int(i) for i in row.split()]
    adj_list.append(next_heads)


num_components = count_components(adj_list)
print(num_components)

