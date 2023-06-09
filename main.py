
def minimum_depth(graph, root):
    if root not in graph:
        return 0

    visited = set()
    queue = [(root, 1)]

    while queue:
        node, depth = queue.pop(0)
        visited.add(node)

        if not any(neighbor in graph for neighbor in graph[node]):
            return depth

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, depth + 1))


def main():
    graph = {}
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        root = int(lines[0].strip())
        for line in lines[1:]:
            node, neighbor = map(int, line.strip().split(','))
            if node not in graph:
                graph[node] = []
            graph[node].append(neighbor)
    with open('output.txt', 'w') as file:
        file.write(str(minimum_depth(graph, root)))


if __name__ == '__main__':
    main()

