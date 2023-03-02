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
            if is_compatible(stations, i, j) and len(res[j]) > len(res[i]):
                res[i] = res[j].copy() 
        res[i] += [stations[i]]
    max_subset = max(res, key=lambda x: len(x))
    print(res)
    if not is_compatible(stations, 0, -1):
        max_subset.remove(stations[-1])
    return max_subset

def is_compatible(stations, i, j):
    prev_dist =  abs((stations[i][0] - stations[j][0]) % 821)
    next_dist =  abs((stations[j][0] - stations[i][0]) % 821)
    if prev_dist < stations[i][1] or next_dist < stations[i][1] or \
       prev_dist < stations[j][1] or next_dist < stations[j][1]:
        return False
    return True
# print(find_gas_stations( [(0, 10), (100, 20), (200, 30), (300, 40)]))
print(find_gas_stations([(0, 20), (200, 150), (400, 200), (400, 1), (405, 5), (410, 4), (600, 250), (800, 20)]))