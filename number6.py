def FB(graph, start_node):
    n = max(max(a,b) for a,b,i in graph) + 1 #число вершин,просто максимальный номер вершины из всех указанных при вводе,
    # ну и нумерация с нуля ж, +1
    distances = [float('inf')] * n
    distances[start_node] = 0

    for i in range(n - 1):
        for a, b, weight in graph:
            if distances[a] != float('inf') and distances[a] + weight < distances[b]: #выгоднее? перезаписываем, туда его
                distances[b] = distances[a] + weight

    for a, b, weight in graph: #как раз тот момент из контрольных вопросов про энную итерацию
        if distances[a] != float('inf') and distances[a] + weight < distances[b]:
            print("Отрицательный цикл") #попаааался
            return None
    return distances

n_eva = int(input("количество ребер: ")) #поняли шутку? типа Ева из ребра Адама и тут как раз рёбра, всё такое
graph = []
for i in range(n_eva):
    a, b, weight = map(int, input().split())
    graph.append((a, b, weight))
start_node = int(input("начальная вершина: "))

distances = FB(graph, start_node)
if distances:
    print("Миним.расстояния от вершины", start_node, ":", distances)
else:
    print("В графе есть отрицательный цикл") #Лошок, попался
