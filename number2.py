def create_matrix(N, edge_list):
  matrix = [[0] * N for i in range(N)]

  for a, b in edge_list:
    matrix[a - 1][b - 1] = 1
  return matrix

N = 4
edge_list = [(1, 2), (1, 3), (2, 4), (3, 1)] #я хотела через ввод сделать,
# но там число рёбер нужно, как в первой задаче, так что будет так((

s_matrix = create_matrix(N, edge_list)
for row in s_matrix:
  print(row)