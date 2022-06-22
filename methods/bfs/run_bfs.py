def bfs(graph, start, end):
    queue = []
    queue.append([start])
    expanded_cost = 0
    visited = set()

    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node in visited:
            continue

        if node == end:
            path_cost = len(path) - 1
            return visited, expanded_cost, path, path_cost

        else:
            for adjacent in graph.get(node, []):
                if adjacent not in visited:
                    new_path = list(path)
                    new_path.append(adjacent)
                    queue.append(new_path)
                    expanded_cost += 1

            visited.add(node)