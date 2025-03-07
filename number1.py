def read_graph():
    N, M = map(int, input().split())
    edge_list = []
    for i in range(M):
        a, b = map(int, input().split())
        edge_list.append((a, b))

    return N, M, edge_list

N, M, edge_list = read_graph()
print(edge_list)

# дальше просто перевод в матрицу связности, что хоть и дублирует вторую задачу почти, но так красивее и удобнее
def s_matrix(n, edge_list):
    matrix = [[0] * n for i in range(n)]
    for a, b in edge_list:
        matrix[a - 1][b - 1] = 1
    return matrix

matrix = s_matrix(N, edge_list)

for row in matrix:
    print(row)
