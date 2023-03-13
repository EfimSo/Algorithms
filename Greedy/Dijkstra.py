# Dijkstra's algorithm: 
# Input:
#   - a dictionary G representing a directed graph 
#     where each node u is mapped to a list of (v, w(v)) pairs where w(v) is the weight of the (u,v) edge
#   - source node s
# Output:
#   - a dictionary of distances from s to every node in G 
#   - a dictionary representing the minimum distance tree from s to every node in G
# example graph used in main is in this folder
import heapq
from math import inf

def Dijkstra(G, s):
    p = dict()  # current best distances 
    d = dict()  # final distances 
    parents = dict()    # minimum distance tree, parents[v] = (u, w) where w is weight of (u,v) edge 
    Q = []      # minheap to keep track of node with smallest distance, keys from p
    for v in G:
        if v == s: continue
        p[v] = inf  # initialize tentative dist for all v != s nodes to infinity
        heapq.heappush(Q, (p[v], v))
    p[s], parents[s] = 0, None  # initialize tentative dist for source to 0
    heapq.heappush(Q, (p[s], s))
    while Q:
        pu, u = heapq.heappop(Q) # pop element with smallest distance (closest); pu = p[u]
        d[u] = pu               # fix distance to tentative distance
        if not G[u]: continue   # handle node with no outgoing neighbors
        for v, wv in G[u]:      # wv is weight of (u,v) edge
            if p[v] > d[u] + wv:    # found shorter path to v
                Q.remove((p[v], v)) # remove current value from heap
                p[v] = d[u] + wv    # update tentative distance to neighbor
                parents[v] = u, wv      # update value in minimum dist tree
                heapq.heappush(Q, (p[v], v))    # push new value to heap
    return d, parents

def find_min_path(G, s, d):
    # finds minimum path using Dijkstra
    _, parents = Dijkstra(G, s)
    curr = d
    path = []
    path_sum = 0
    while curr in parents and parents[curr] is not None:
        path.append(curr)
        parent, dist = parents[curr] # distance is the weight of (parent, curr) edge
        path_sum += dist
        curr = parent
    if curr != s: return None, None  # no path exists
    path.append(s)
    return path[::-1], path_sum  



def main():
    G = dict()
    G["s"] = [("a", 15), ("b", 6), ("c", 2)]
    G["a"] = []
    G["b"] = [("a", 1), ("e", 2)]
    G["c"] = [("d", 8), ("e", 8)]
    G["d"] = [("a", 3)]
    G["e"] = [("d", 1)]
    # dist, parents = Dijkstra(G, "s")
    # print(dist, parents)
    path, sum = find_min_path(G, "e", "a")
    print("path: ", path)
    print("distance: ", sum)
main()