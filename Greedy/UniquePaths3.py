
# Online Python - IDE, Editor, Compiler, Interpreter
from Dijkstra import Dijkstra
from math import inf

# algorithm that returns the edges of two distinct paths from s to x given graph G,
# source node s and destination node x which is known to have multiple shortest paths from s
# current issue: does not work correctly when backtracking only one node
# correct reversing the list twice in DFS and find_two_shortest_paths
def find_two_shortest_paths(G, s, x):
    # helper function for edge printing    
    def get_edges(nodes):
        res = []
        for i in range(1, len(nodes)):
            res.append((nodes[i-1], nodes[i]))
        return res
    # finds minimum path using Dijkstra
    dist, parents = Dijkstra(G, s)
    if dist[x] == inf:
        return None, None   # x is not reachable from s
    curr = parents[x]
    path1 = [x]
    path_set = {x}
    visited = {x}
    path2 = []
    found = False
    while curr is not None:
        path1.append(curr)
        path_set.add(curr)
        visited.add(curr)
        if found:
            path2.append(curr)
        else:
            path, node = DFS(G, dist, curr, path_set, visited)
            if node is not None:
                found = True
                for n in path1:     # append section of path1 before node to path2
                    if n == node:
                        break
                    path2.append(n)
                path2.extend(path)
        curr = parents[curr]
    # return get_edges(path1[::-1]), get_edges(path2[::-1])     # uncomment to get edges
    return path1[::-1], path2[::-1]

def DFS(G, distances, s, pset, visited):
    def recur(u, length, path, found):
        visited.add(u)
        if not G[u]: pass
        else:
            for v, wv in G[u]:
                # print(f"node: {u}, neighbor: {v}, length: {length}, weight: {wv}, d: {distances[v]}, found: {found}")
                if v in pset:
                    if u in pset:       # skip node if going from one node in path to another in 1 step
                        continue
                    if length + wv == distances[v]:
                        path.append(v)
                        path.append(u)
                        return v
                if v not in visited:
                    n = recur(v, length + wv, path, found)
                    if n is not None:
                        found = True
                        break
        if found:
            path.append(u)
            return n
        else:
            return None
    path = []
    node = recur(s, distances[s], path, False)
    if node is not None:
        return path, node
    else:
        return [], None


def main():
    G = dict()
    G["s"] = [("a", 8), ("b", 6), ("c", 2)]
    G["a"] = []
    G["b"] = [("a", 2), ("e", 2)]
    G["c"] = [("d", 8), ("e", 7)]
    G["d"] = [("a", 3)]
    G["e"] = [("d", 1)]
    # p1, p2 = find_two_shortest_paths(G, "s", "d")
    p3, p4 = find_two_shortest_paths(G, "c", "a")
    # print(p1, p2)
    print(p3, p4)
main()