# Given a 2D array (i.e., a matrix) containing only 1s (land) and 0s (water),
# count the number of islands in it.
# An island is a connected set of 1s (land) and is surrounded by either an edge or 0s (water).
from collections import deque

def count_islands(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    total_islands = 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                total_islands += 1
                # search_island_dfs(matrix, i, j)
                search_island_bfs(matrix, i, j)

    return total_islands


def search_island_dfs(matrix, i, j):
    if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]):   # handle out of bounds
        return
    if matrix[i][j] == 0:   # handle water cell
        return

    matrix[i][j] = 0

    search_island_dfs(matrix, i + 1, j)
    search_island_dfs(matrix, i - 1, j)
    search_island_dfs(matrix, i, j + 1)
    search_island_dfs(matrix, i, j - 1)

def search_island_bfs(matrix, i, j):
    q = deque([(i, j)])

    while q:
        x, y = q.popleft()
        if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):   # handle out of bounds
            continue
        if matrix[x][y] == 0:   # handle water cell
            continue

        matrix[x][y] = 0
        q.extend([(x + 1, y)])
        q.extend([(x - 1, y)])
        q.extend([(x, y + 1)])
        q.extend([(x, y - 1)])



def main():
    print(count_islands([[0, 1, 1, 1, 0], 
                         [0, 0, 0, 1, 1], 
                         [0, 1, 1, 1, 0],
                         [0, 1, 1, 0, 0],
                         [0, 0, 0, 0, 0]]))

    print(count_islands([[1, 1, 1, 0, 0],
                         [0, 1, 0, 0, 1],
                         [0, 0, 1, 1, 0],
                         [0, 0, 1, 0, 0],
                         [0, 0, 1, 0, 0]]))


main()