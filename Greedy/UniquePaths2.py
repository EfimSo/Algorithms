from Dijkstra import Dijkstra
from math import inf
import heapq as hq

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
    # prev = x
    curr = parents[x]
    # distance = 0
    path1 = [x]
    path_set = {x}
    path2 = []
    found = False
    done = False
    visited = set()
    while curr is not None:
        path1.append(curr)
        path_set.add(curr)
        if done:
            path2.append(curr)
        else:
            print(path_set)
            distance, path, found, node = DFS(G, curr, x, path_set, dist[curr], visited)
            if found and distance == dist[node]:
                print(f"node: {node}, distance: {distance}, dist: {dist[node]}")
                done = True
                print(f"path: {path}")
                path2.extend(path)
        # prev = curr
        curr = parents[curr]
    # return get_edges(path1[::-1]), get_edges(path2[::-1])
    # print(dist[x])
    return path1[::-1], path2[::-1]

def DFS(G, s, d, pset, start_distance, visited):
    # add path length?
    def recur(u, weight, length, num_nodes, path, found):
        print(f"node: {u}", f"path length: {num_nodes}")
        if u == d:
            path.append(u)
            return length + weight, True, u
        visited.add(u)
        if not G[u]: pass
        else:
            for v, wv in G[u]:
                if v in pset:
                    if u in pset:
                        continue
                    path.append(v)
                    path.append(u)
                    return length + weight + wv, True, v
                if v not in visited:
                    l, f, n = recur(v, wv, length, num_nodes + 1, path, found)
                    if f:
                        found = True
                        length = l
                        break
        if found:
            path.append(u)
            return length + weight, True, u
        else:
            visited.remove(u)
            return length, False, None
    path = []
    length, found, node = recur(s, 0, 0, 0, path, False)
    if found:
        return start_distance + length, path, True, node
    else:
        return -1, [], False, None


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
    p1, p2 = find_two_shortest_paths(G, "s", "e")
    print(p1, p2)
main()
