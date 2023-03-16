# Given n 4-tuples train(i) = (depcity(i), arrcity(i), dep(i), arr(i)) where
# each tuple is a train leaving depcity(i) at dep(i) and arriving
# to arrcity(i) at arr(i) and a starting city,
# return the shortest time you can travel from your city to every other one
# uses a version of Dijkstra with a min heap
from heapq import heappush, heappop
from math import inf
from Dijkstra import Dijkstra

def find_cities(cities, s): # s = starting city
    G = {depcity: [] for depcity, *other in cities}
    G.update({arrcity: [] for depcity, arrcity, *other in cities})
    for depcity, arrcity, dept, arrt in cities:
        G[depcity].append((arrcity, dept, arrt))
    Q = [(0, s)]
    set_cities = {s}
    for  depcity, arrcity, dept, arrt in cities:
        if depcity not in set_cities:
            Q.append((inf, depcity))
            set_cities.add(depcity)
        if arrcity not in set_cities:
            Q.append((inf, arrcity))
            set_cities.add(arrcity)
    # Q.extend([(inf, depcity) for depcity, *other in cities])
    p = {depcity: 0 if depcity == s else inf for depcity, *other in cities} # earliest known time you can arrive at a city
    p.update({arrcity: inf for depcity, arrcity, *other in cities if arrcity not in p})
    dist = dict()
    while Q:
        earliest_arr_time, dep_city = heappop(Q)
        dist[dep_city] = earliest_arr_time
        if G[dep_city]:
            for arr_city, dep_time, arr_time in G[dep_city]:
                if dep_time >= earliest_arr_time and p[arr_city] > arr_time:
                    # try: Q.remove((p[arr_city], arr_city)) 
                    # except ValueError: pass 
                    Q.remove((p[arr_city], arr_city)) 
                    p[arr_city] = arr_time
                    heappush(Q, (p[arr_city], arr_city))
    return dist

def find_cities2(cities, s):
    G = {depcity: [] for depcity, *other in cities}
    G.update({arrcity: [] for depcity, arrcity, *other in cities if arrcity not in G})
    for depcity, arrcity, dept, arrt in cities:
        G[depcity].append((arrcity, arrt - dept))
    d, parents = Dijkstra(G, s)
    return d
# have to set distance to the arrival time not previous time + difference
# sort by arrival time instead of difference?
def main():
    start_city = 'A'
    # train_schedule = [('A', 'B', 0, 5), ('A', 'C', 0, 10), ('B', 'C', 5, 8), ('C', 'D', 10, 15)]
    # train_schedule = [('A', 'B', 0, 2), ('A', 'C', 0, 3), ('B', 'C', 2, 3), ('B', 'D', 2, 6), ('C', 'D', 3, 6)]
    train_schedule = [('A', 'B', 0, 5), ('B', 'C', 5, 6), ('C', 'D', 10, 15), ('B', 'D', 4, 7)]

    distances = find_cities(train_schedule, start_city)
    print(distances)
main()