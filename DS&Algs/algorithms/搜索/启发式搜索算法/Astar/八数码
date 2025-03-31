import heapq

def str_to_list(state_str):
    return [[int(state_str[3 * i + j]) for j in range(3)] for i in range(3)]

def list_to_str(state):
    return ''.join([str(i) for row in state for i in row] )

def distance(state, goal):
    goal_str = list_to_str(goal)
    d = 0
    for i in range(3):
        for j in range(3):
            x, y = divmod(goal_str.index(str(state[i][j])), 3)
            d += abs(i - x) + abs(j - y)
    return d

def blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def move(state):
    neighbors = []
    x, y = blank(state)
    d = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    for dx, dy in d:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

def A_star(state, goal):
    state_str = list_to_str(state)
    goal_str = list_to_str(goal)
    come_from = {state_str: None}
    heap = []
    heapq.heappush(heap, (0, state_str))
    g = {state_str: 0}
    f = {state_str: distance(state, goal)}

    while heap :
        _, current_str = heapq.heappop(heap)
        current = str_to_list(current_str)
        if current_str == goal_str:
            path = []
            while current_str:
                path.append(str_to_list(current_str))
                current_str = come_from[current_str]
            return path[::-1]
        for neighbor in move(current):
            neighbor_str = list_to_str(neighbor)
            g_score = g[current_str] + 1
            if neighbor_str not in g or g_score < g[neighbor_str]:
                g[neighbor_str] = g_score
                f[neighbor_str] = g_score + distance(neighbor, goal)
                come_from[neighbor_str] = current_str
                if neighbor_str not in [i[1] for i in heap]:
                    heapq.heappush(heap, (f[neighbor_str], neighbor_str))
    return None

start_state = [
    [3, 7, 5],
    [2, 0, 4],
    [1, 6, 8]
]
goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

path = A_star(start_state, goal_state)

if path:
    for step in path:
        for row in step:
            print(row)
        print()

else:
    print('No way found')