def dfs(graph, start, visited=None):
    if visited is None:
        visited = []

    if start not in visited:
        print(start, end=" ")
        visited.append(start)

        for neighbour in graph[start]:
            dfs(graph, neighbour, visited)
