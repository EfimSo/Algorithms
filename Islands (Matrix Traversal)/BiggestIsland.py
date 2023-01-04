# Given a 2D array (i.e., a matrix) containing only 1s (land) and 0s (water), find the biggest island in it.
# Write a function to return the area of the biggest island. 
# An island is a connected set of 1s (land) and is surrounded by either an edge or 0s (water).
from collections import deque

def find_biggest_island(matrix):
    max_area = 0
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                # area = visit_island_dfs(matrix, i, j)
                area = visit_island_bfs(matrix, i, j)
                max_area = max(max_area, area)
    return max_area

def visit_island_dfs(matrix, i, j):
    if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]):   # handle out of bounds
        return 0
    if matrix[i][j] == 0:   # handle water cell
        return 0
    
    matrix[i][j] = 0
    res_area = 1
    res_area += visit_island_dfs(matrix, i + 1, j)
    res_area += visit_island_dfs(matrix, i - 1, j)
    res_area += visit_island_dfs(matrix, i, j + 1)
    res_area += visit_island_dfs(matrix, i, j - 1)

    return res_area

def visit_island_bfs(matrix, i, j):
    q = deque([(i, j)])
    area = 0

    while q:
        x, y = q.popleft()
        if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):   # handle out of bounds
            continue
        if matrix[x][y] == 0:   # handle water cell
            continue

        matrix[x][y] = 0
        area += 1

        q.extend([(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)])

    return area

def main():
    print(find_biggest_island([[0, 1, 1, 1, 0], 
                         [0, 0, 0, 1, 1], 
                         [0, 1, 1, 1, 0],
                         [0, 1, 1, 0, 0],
                         [0, 0, 0, 0, 0]]))

    print(find_biggest_island([[1, 1, 1, 0, 0],
                         [0, 1, 0, 0, 1],
                         [0, 0, 1, 1, 0],
                         [0, 0, 1, 0, 0],
                         [0, 0, 1, 0, 0]]))

    print(find_biggest_island([[1, 1, 1, 0, 0], [0, 1, 0, 0, 1], [
          0, 0, 1, 1, 0], [0, 1, 1, 0, 0], [0, 0, 1, 0, 0]]))

main()