# 10*10迷宫，起点为(0, 0)，终点为(9, 9)

maze = [
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0]
]


def bfs_explore():
    d = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    queue = [(0, 0)]
    come_from = {(0, 0): None}
    visited = set()
    while queue:
        x, y = queue.pop(0)
        visited.add((x, y))
        if (x, y) == (9, 9):
            current = (9, 9)
            path = []
            while current:
                path.append(current)
                current = come_from[current]
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 10 and 0 <= ny < 10 and maze[nx][ny] == 0 and (nx, ny) not in visited:
                queue.append((nx, ny))
                come_from[(nx, ny)] = (x, y)
    return path[::-1]

path = bfs_explore()
print(path)