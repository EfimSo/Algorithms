# recursive implementation of DFS on a graph. Finds start and finish time and DFS tree
# top_order uses the finish time for topological sort
# example graph used in main is found in ./GraphDFS.png
def DFS(G, s):
    parents = dict()
    times = {v: [-1, -1] for v in G}
    visited = {s}
    parents[s] = None
    t = [-1]
    def recur(u):
        visited.add(u)
        t[0] += 1
        times[u][0] = t[0]
        for v in sorted(G[u]):
            if v not in visited:
                parents[v] = u
                recur(v)
        t[0] += 1
        times[u][1] = t[0]
    recur(s)
    return times, parents

def top_sort(G):
    indegree = {v: 0 for v in G}
    for u in G:
        for v in G[u]:
            indegree[v] += 1
    times, parents = {}, {}
    for v in indegree:
        if indegree[v] == 0:
            times, parents = DFS(G, v)
            break   # assumes only one start node, could be updated
    top_order = sorted(times.keys(), key=lambda x: times[x][1], reverse=True) # sort by decreasing order of finish time
    return top_order


def main():
    G = dict()
    G["a"] = ["b", "c"]
    G["b"] = ["e"]
    G["c"] = ["d", "e"]
    G["d"] = ["e", "g"]
    G["e"] = ["f", "h"]
    G["f"] = []
    G["g"] = ["j"]
    G["h"] = []
    G["i"] = ["f"]
    G["j"] = ["k"]
    G["k"] = ["l", "m"]
    G["l"] = ["i"]
    G["m"] = []
    times, parents = DFS(G, "a")
    print(f"times: {times}")
    print(f"parents: {parents}")
    print(f"topological order: {top_sort(G)}")
main()