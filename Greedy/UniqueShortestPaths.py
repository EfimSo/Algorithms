from Dijkstra import Dijkstra
from math import inf
import heapq as hq
from functools import reduce

# modified Dijkstra algorithm that also returns a dictionary indicating if
# each node has only one unique shortest path from the source
def Dijkstra_unique(G, s):
    p = dict()  # current best distances 
    d = dict()  # final distances 
    parents = dict()    # minimum distance tree, parents[v] = u where (u,v) is an edge in the tree 
    UNIQUE = {v: True for v in G}     # dictionary of True/False values for uniqueness of shortest path to each v 
    Q = []      # minheap to keep track of node with smallest distance, keys from p
    for v in G:
        if v == s: continue
        p[v] = inf  # initialize tentative dist for all v != s nodes to infinity
        hq.heappush(Q, (p[v], v))
    p[s], parents[s] = 0, None  # initialize tentative dist for source to 0
    hq.heappush(Q, (p[s], s))
    while Q:
        pu, u = hq.heappop(Q) # pop element with smallest distance (closest); pu = p[u]
        d[u] = pu               # fix distance to tentative distance
        if not G[u]: continue   # handle node with no outgoing neighbors
        for v, wv in G[u]:      # wv is weight of (u,v) edge
            if p[v] == d[u] + wv:
                UNIQUE[v] = False
            elif p[v] > d[u] + wv:    # found shorter path to v
                Q.remove((p[v], v)) # remove current value from heap
                p[v] = d[u] + wv    # update tentative distance to neighbor
                parents[v] = u      # update value in minimum dist tree
                hq.heappush(Q, (p[v], v))    # push new value to heap
                UNIQUE[v] = True
    for v in UNIQUE:
        if d[v] == inf:
            UNIQUE[v] = False
    return d, parents, UNIQUE

# algorithm that returns the edges of two distinct paths from s to x given graph G,
# source node s and destination node x which is known to have multiple shortest paths from s
# current issue: does not work correctly when backtracking only one node
# correct reversing the list twice in DFS and find_two_shortest_paths
def find_two_shortest_paths(G, s, x):
    # helper function for edge printing    
    def get_edges(nodes: list[str]):
        res = []
        for i in range(1, len(nodes)):
            res.append((nodes[i-1], nodes[i]))
        return res
    # finds minimum path using Dijkstra
    dist, parents = Dijkstra(G, s)
    if dist[x] == inf:
        return None, None   # x is not reachable from s
    prev = x
    curr = parents[x]
    # distance = 0
    path1 = [x]
    path2 = []
    found = False
    done = False
    visited = set()
    while curr is not None:
        path1.append(curr)
        if done:
            path2.append(curr)
        else:
            distance, path, found = DFS(G, curr, prev, x, dist[curr], visited)
            if found and distance == dist[x]:
                done = True
                path2.extend(path)
        prev = curr
        curr = parents[curr]
    # return get_edges(path1[::-1]), get_edges(path2[::-1])
    print(dist[x])
    return path1[::-1], path2[::-1]

def DFS(G, s, prev, d, start_distance, visited):
    # add path length?
    def recur(u, weight, length, num_nodes, path, found):
        print(f"node: {u}", f"path length: {num_nodes}", f"prev: {prev}")
        if u == prev and num_nodes == 1:
            return -1, False
        if u == d:
            path.append(d)
            return length + weight, True
        visited.add(u)
        if not G[u]: pass
        else:
            for v, wv in G[u]:
                if v not in visited:
                    l, f = recur(v, wv, length, num_nodes + 1, path, found)
                    if f:
                        found = True
                        length = l
                        break
        if found:
            path.append(u)
            return length + weight, True
        else:
            visited.remove(u)
            return length, False
    path = []
    length, found = recur(s, 0, 0, 0, path, False)
    if found:
        return start_distance + length, path, True
    else:
        return -1, [], False


def main():
    G = dict()
    G["s"] = [("a", 8), ("b", 6), ("c", 2)]
    G["a"] = []
    G["b"] = [("a", 2), ("e", 2)]
    G["c"] = [("d", 8), ("e", 6)]
    G["d"] = [("a", 3)]
    G["e"] = [("d", 1)]
    # dist, parents, unique = Dijkstra_unique(G, "a")
    # print(f"Distances: {dist}")
    # print(f"Parents: {parents}")
    # print(f"Uniqueness: {unique}")

    # path, dist = find_min_path(G, "s", "d")
    # print(f"path: {path}")
    # print(f"distance: {dist}") 
    # visited = set()
    # print(DFS(G, "s", "c", 0, visited))
    p1, p2 = find_two_shortest_paths(G, "s", "d")
    print(p1, p2)
main()
