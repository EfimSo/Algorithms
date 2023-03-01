# Given a list of pairs [location, distance] of gas stations on a circular 821 road where 
# location is the mile on the road of the gas station 
# and distance is the minimum distance until another gas station,
# find the maximum compatible subset of gas stations to be built
def find_gas_stations(stations):
    # sort in increasing order of location
    stations.sort()
    n = len(stations)
    res = [[] for i in range(n)]
    res[0].append(stations[0])
    for i in range(1, n):
        for j in range(i):
            if is_compatible(stations, i, j) and is_compatible(stations, j, i): # is this right? 
                res[i] = res[j].copy()
        res[i] += [stations[i]]
    max_subset = max(res, key=lambda x: len(x))
    print(res)
    # is this right? 
    if not (is_compatible(stations, -1, 0) and is_compatible(stations, 0, -1)):
        max_subset.remove(stations[-1])
    return max_subset

def is_compatible(stations, i, j):
    prev_dist =  (stations[i][0] - stations[j][0]) % 821
    next_dist =  (stations[j][0] - stations[i][0]) % 821
    if not (abs(prev_dist) < stations[i][1] or abs(next_dist) < stations[i][1]):
        return True
    return False
# print(find_gas_stations( [(0, 10), (100, 20), (200, 30), (300, 40)]))
print(find_gas_stations([(0, 50), (200, 150), (400, 200), (600, 250), (800, 20)]))