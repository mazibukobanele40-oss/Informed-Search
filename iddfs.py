def dls(graph, node, depth):
    if depth < 0:
        return

    print(node, end=" ")

    if depth == 0:
        return

    for neighbour in graph[node]:
        dls(graph, neighbour, depth - 1)


def iddfs(graph, start, max_depth):
    for depth in range(max_depth + 1):
        print(f"\nDepth {depth}:", end=" ")
        dls(graph, start, depth)
