# implementation of the Bellman-Ford algorithm
# given a destination vertex, finds the shortest path from each vertex to the destination vertex
from math import inf
def bellman_ford(G, t):
    children = dict()       # keeps track of the first element on the path v -> t
    n = len(G.keys())
    M = dict()      # M[(i, v)] = OPT[i, v] = Optimal solution to get from v to t in at most i edges
    
    for v in G:
        if v == t:
            continue
        M[(0, v)] = inf
        children[v] = None
    M[(0, t)] = 0
    children[t] = None

    for i in range(1, n):
        for v in G:
            M[(i, v)] = M[(i-1, v)]
            for u, wu in G[v]:
                if M[(i, v)] > wu + M[(i-1, u)]:
                    M[(i, v)] = wu + M[(i-1, u)]
                    children[v] = u
    return M, children

def backtrack(children, s):
    path = [s]
    v = s
    while children[v] is not None:
        v = children[v]
        path.append(v)
    return path

def main():
    G = dict()
    G["s"] = [("a", 15), ("b", 6), ("c", 2)]
    G["a"] = []
    G["b"] = [("a", 1), ("e", 2)]
    G["c"] = [("d", 8), ("e", 8)]
    G["d"] = [("a", 3)]
    G["e"] = [("d", 1)]
    M, children = bellman_ford(G, "d")
    print(f"M: {M}")
    print(f"children: {children}")
    print({v: [M[(i, v)] for i in range(len(G.keys()))] for v in G})
    path = backtrack(children, "s")
    print(f"path: {path}")
main()