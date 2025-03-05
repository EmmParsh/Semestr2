def trans_matrix(matrix):
  n = len(matrix)
  t_matrix = [[0] * n for l in range(n)]
  for i in range(n):
    for j in range(n):
      t_matrix[j][i] = matrix[i][j]
  return t_matrix
# matrix =[
#   [0, 1, 0, 0],
#   [0, 0, 1, 1],
#   [0, 0, 0, 0],
#   [0, 0, 0, 0]
# ]
#или матрицу через ввод сделать, но для этого нужен её размер, что нам не дан, но ниже сделаю так, будто дан:
matrix = []
n = int(input())
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

t_matrix = trans_matrix(matrix)
for row in t_matrix:
  print(row)