# Graph BFS implementation using a queue
# example graph used in main is found at ./GraphBFS.png
from collections import deque

def BFS(G, s):
    dist, parents = {}, {}
    Q = deque()
    Q.append(s)
    parents[s] = None
    dist[s] = 0
    while Q:
        u = Q.popleft()
        for v in sorted(G[u]):  # iterate through neighbors in alphabetical order (doesn't matter)
            if v not in parents:
                parents[v] = u
                dist[v] = dist[u] + 1
                Q.append(v)
    return dist, parents

# checks if a graph is bipartite by checking if there exists an edge between 
# two nodes in the same layer of the BFS search tree
def is_bipartite(G, s):
    dist, parents = BFS(G, s)
    bipartite = True
    edges_to_remove = [] # if not bipartite, the edges that need to be removed will be added to here
    for u in dist:
        for v in G[u]:
            if dist[u] == dist[v]:
                bipartite = False
                edges_to_remove.append((u, v))
    return bipartite, edges_to_remove
    

def main():
    G = dict()
    G["s"] = ["a", "b", "c"]
    G["a"] = ["d", "g", "s"]
    G["b"] = ["s", "e", "f"]
    G["c"] = ["s", "d", "e"]
    G["d"] = ["a", "c", "h"]
    G["e"] = ["c", "b", "h", "g", "i"]
    G["f"] = ["b", "h"]
    G["g"] = ["a", "e", "i"]
    G["h"] = ["d", "e", "f"]
    G["i"] = ["g", "e"]
    dist, parents = BFS(G, "s")
    print(f"dist: {dist}")
    print(f"parents: {parents}")
    is_bip, edges = is_bipartite(G, "s")
    print(f"bipartite?: {is_bip}")
    print(f"edges to remove: {edges}")
main()
