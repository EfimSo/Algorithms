# implementation of the Bellman-Ford algorithm
# given a destination vertex, finds the shortest path from each vertex to the destination vertex
from math import inf
# finds minimal distances to reach t from each node v != t in G
# M[n-1, v] will contain the solution for each v
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

# easier version that finds distances to all nodes from a source - same as Dijkstra
def bellman_ford2(G, s):
    dist = {}
    parents = {}
    for v in G:
        dist[v] = inf
        parents[v] = None
    dist[s] = 0
    n = len(G.keys())
    for i in range(n-1):
        for v in G:
            if dist[v] == inf:
                continue
            for u, wu in G[v]:
                if dist[u] > dist[v] + wu:
                    dist[u] = dist[v] + wu
                    parents[u] = v
    return dist, parents

def backtrack2(dist, parents, d):
    if dist[d] == inf:
        return []   # d is not reachable from s
    curr = d
    path = []
    while curr is not None:
        path.append(curr)
        curr = parents[curr]
    return path[::-1]


def main():
    # refer to ./../Dijkstra/Dijkstra.png for an image of the testing graph
    G = dict()
    G["s"] = [("a", 15), ("b", 6), ("c", 2)]
    G["a"] = []
    G["b"] = [("a", 1), ("e", 2)]
    G["c"] = [("d", 8), ("e", 8)]
    G["d"] = [("a", 3)]
    G["e"] = [("d", 1)]
    # M, children = bellman_ford(G, "d")
    # print(f"M: {M}")
    # print(f"children: {children}")
    # print({v: [M[(i, v)] for i in range(len(G.keys()))] for v in G})
    # path = backtrack(children, "s")
    # print(f"path: {path}")
    dist, parents = bellman_ford2(G, "s")
    print(f"dist: {dist}")
    print(f"parents: {parents}")
    path = backtrack2(dist, parents, "d")
    print(f"path: {path}")
main()