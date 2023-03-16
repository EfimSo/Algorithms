# Given n 4-tuples train(i) = (depcity(i), arrcity(i), dep(i), arr(i)) where
# each tuple is a train leaving depcity(i) at dep(i) and arriving
# to arrcity(i) at arr(i) and a starting city,
# return the earliest time you can travel from your city to every other one
# uses a version of Dijkstra with a min heap
from heapq import heapify, heappush, heappop
from math import inf
from Dijkstra import Dijkstra

def find_cities(trains, s): # s = starting city
    cities = set()
    for depcity, arrcity, dept, arrt in trains:
        cities.add(depcity)
        cities.add(arrcity)
    G = {city: [] for city in cities}
    for depcity, arrcity, dept, arrt in trains:
        G[depcity].append((arrcity, dept, arrt))
    Q = [(0 if city == s else inf, city) for city in cities]
    heapify(Q)
    p = {city: 0 if city == s else inf for city in cities} # earliest known time you can arrive at a city
    dist = dict()
    while Q:
        earliest_arr_time, dep_city = heappop(Q)
        dist[dep_city] = earliest_arr_time
        if G[dep_city]:
            for arr_city, dep_time, arr_time in G[dep_city]:
                if dep_time >= earliest_arr_time and p[arr_city] > arr_time:
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
    train_schedule = [('A', 'B', 0, 2), ('A', 'C', 0, 3), ('B', 'C', 2, 3), ('B', 'D', 2, 6), ('C', 'D', 3, 7)]
    # train_schedule = [('A', 'B', 0, 5), ('B', 'C', 5, 6), ('C', 'D', 10, 15), ('B', 'D', 4, 7)]
    distances = find_cities(train_schedule, start_city)
    print(distances)
main()