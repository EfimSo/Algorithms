# You are given an n×m board B with some amount of coins in each cell. Traverse the board
# from the top left to the bottom right corner of B, collecting the coins in each cell that you
# step on. (You will always collect the value in the top left and bottom right corners.) During
# the traversal you can only step into an adjacent cell either to the right or below your current
# location. That is, from B[i, j] you can only go to B[i + 1, j] or B[i, j + 1]. Find the best
# route to collect the maximum total amount of coins. The input to your algorithm is a table
# B with B[i, j] containing the money amount at location [i, j].

def trav_mat(B):
    n, m = len(B), len(B[0])
    M = [[0 for _ in range(n)] for _ in range(m)]
    C = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                M[i][j] = B[i][j]
                C[i][j] = -1
            elif i == 0:
                M[i][j] = B[i][j] + M[i][j-1]
                C[i][j] = j-1
            elif j == 0:
                M[i][j] = B[i][j] + M[i-1][j]
                C[i][j] = i-1
            else:
                M[i][j] = B[i][j] + max(M[i-1][j], M[i][j-1])
                if M[i-1][j] > M[i][j-1]:
                    C[i][j] = i-1
                else:
                    C[i][j] = j-1
    return M, C

def backtrack(B, C, i, j):
    n, m = len(B), len(B[0])
    if i >= n or j >= m: return None
    path = []
    k, t = i, j
    while k >= 0 and t >= 0:
        path.append(B[k][t])
        if C[k][t] == k-1:
            k -= 1
        else:
            t -= 1
    return path
                
            
    