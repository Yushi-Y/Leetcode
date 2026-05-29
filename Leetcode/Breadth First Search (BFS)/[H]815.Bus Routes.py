### Thinking First
# What do we need to track?

# How many buses we've taken so far
# Which stops we've already visited (don't revisit)
# Which bus routes we've already used (don't revisit)

# How do we move?
# From a stop → find all buses serving that stop
# Board that bus → instantly access ALL stops on that route
# From those new stops → find more buses

# When do we stop?
# The moment we see target → return buses count
# Queue runs empty → return -1

# Why Separate Routes and Stops
# Routes are what we count — each new route boarded = +1 bus
# Stops are how we move between routes — a shared stop is where you switch buses
# We bridge them through a stop to route dictionary

# visited_stops (notebook) — remembers every stop we've ever seen (prevents revisiting)
# queue (to-do list) — holds only the stops we still need to process

### Pseudocode
    # stop_to_route = {}

    #     if source == target:
    #         return 0
        
    #     # build reverse map so we can go stop → routes (routes are the numbers we count)
    #     for each route i:
    #         for each stop in that route:
    #             stop_to_route[stop].add(i)

    #     # set up BFS
    #     queue = [source]
    #     visited_stops = [source]
    #     visited_routes = {}
    #     buses = 0

    #     # BFS loop
    #     while queue not empty:
    #         buses += 1
    #         for each stop in current level:
    #             for each route serving this stop:
    #                 if route visited: skip
    #                 mark route visited
    #                 for each stop in this route:
    #                     if stop == target:
    #                         return buses
    #                     if stop not visited:
    #                         mark stop visited
    #                         add stop to visited_stops


### Queue is leveled at buses = i
# routes = [[1,2,7],[3,6,7]], source = 1, target = 6

# Start:
# queue = [1]
# buses = 0

# buses = 1, process level 1 — queue has 1 stop:
# pop stop 1
#   → board Bus 0 (stops 1,2,7)
#   → discover stops 2, 7
#   → add to queue

# queue = [2, 7]

# buses = 2, process level 2 — queue has 2 stops:
# pop stop 2
#   → Bus 0 already visited, skip

# pop stop 7
#   → board Bus 1 (stops 3,6,7)
#   → discover stop 3, 6
#   → stop 6 == target! return 2 ✅

# So the queue grows and shrinks like this:
# [1]          ← level 1 (1 stop to process)
# [2, 7]       ← level 2 (2 stops to process)
# never gets to level 3 — found target!


### Why need deque
# A regular Python list has pop() which removes from the end:
# pythonqueue = [2, 7]
# queue.pop()  # removes 7 (wrong — we want 2 first)
# BFS needs to process stops in the order they were added — first in, first out. So we need to remove from the front.
# On a regular list, removing from the front is slow — O(n) — because Python shifts every element across.
# deque (double ended queue) is designed exactly for this — popleft() removes from the front in O(1).


### TC and SC
# can safely assume n >> m normally, n is number of routes, m is number of buses
# TC: O(n) where n is number of stops across all routes
#    for i, route in enumerate(routes):
            # for stop in route:
# for route_index in stop_to_route[stop]: # every route at a stop
#     for stop in routes[route_index]:     # every stop in that route
    
# SC:O(n)
# visited_stops and queue: both are O(N).
# stop_to_route is also O(N) since it stores every stop across all routes.

from collections import defaultdict, deque

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        stop_to_route = defaultdict(set) # create an empty set for any non-existing key

        if source == target:
            return 0
        
        # build reverse map so we can go stop → routes (routes are the numbers we count)
        # add the 'route index' to dict, not the entire route list
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_route[stop].add(i)

        # set up BFS
        queue = deque([source])
        visited_stops = {source}
        visited_routes = set() # set of route indexes, O(1) for element look up, vs O(n) for a list
        buses = 0

        # BFS loop
        while queue: # not empty
            buses += 1
            for _ in range(len(queue)):
                stop = queue.popleft() # first stop in queue at this buses = i level - take a snapshot
                for route_index in stop_to_route[stop]:
                    # if route_index is in visited routes, skip
                    if route_index not in visited_routes: 
                        visited_routes.add(route_index)
                        for stop in routes[route_index]:
                            if stop == target:
                                return buses # return actual numbers inside the loop
                            if stop not in visited_stops:
                                visited_stops.add(stop)
                                queue.append(stop)

        return -1 # if no target found



    