
loot = [1, 10, 15, 10, 3]
def pirate_loot(v):
    n = len(v)
    memo = {}
    def dp(i, j):
        if i > j:
            return 0
        if i == j:
            return v[i]
        if (i, j) in memo:
            return memo[(i, j)]
        left = v[i] + min(dp(i+2, j), dp(i+1, j-1))
        right = v[j] + min(dp(i+1, j-1), dp(i, j-2))
        memo[(i, j)] = max(left, right)
        return memo[(i, j)]
    
    def backtrack():
        res = []
        def recur(i, j):
            if i > j:
                return 0
            left = v[i] + min(memo[(i+2, j)], memo[(i+1, j-1)])
            right = v[j] + min(memo[(i+1, j-1)], memo[(i, j-2)])
            if left > right:
                res.append(v[i])
                recur(*min((i+2, j), (i+1, j-1), key=lambda x: memo[(x[0], x[1])]))
            else:
                res.append(v[j])
                recur(*min((i+1, j-1), (i, j-2), key=lambda x: memo[(x[0], x[1])]))
        recur(0, n-1)
        return res[::-1]
    dp(0, n-1)
    for i in range(n):
        memo[(i, i)] = v[i]
    return backtrack(), memo 