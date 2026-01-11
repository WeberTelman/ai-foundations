# Simple maze solver using DFS

maze = [
    ["S", ".", ".", "#", "."],
    ["#", "#", ".", "#", "."],
    [".", ".", ".", ".", "."],
    ["#", ".", "#", "#", "."],
    [".", ".", ".", "E", "#"]
]

rows = len(maze)
cols = len(maze[0])

def find_start():
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == "S":
                return (i, j)

def dfs(x, y, visited):
    if x < 0 or y < 0 or x >= rows or y >= cols:
        return False
    if maze[x][y] == "#" or (x, y) in visited:
        return False
    if maze[x][y] == "E":
        print("Exit found!")
        return True

    visited.add((x, y))

    if dfs(x+1, y, visited): return True
    if dfs(x-1, y, visited): return True
    if dfs(x, y+1, visited): return True
    if dfs(x, y-1, visited): return True

    return False

start = find_start()
dfs(start[0], start[1], set())
