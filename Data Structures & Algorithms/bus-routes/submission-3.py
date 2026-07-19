from collections import deque, defaultdict

class Solution:
    '''
    BFS through stops on each route to find target (each route is a 'layer'). Each time we go to a new route, we increment the number of buses/routes taken.

    Map the stops to the routes it's in.
    routesMaps = stop : [r0, r1,..]
    1 : r0
    2 : r0
    7 : r0, r1
    3 : r1
    6 : r1
    

    Time Complexity: 
    Space Complexity:
    Time spent on problem:
    '''
    from collections import defaultdict, deque
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:

        # Step 1: build routesMap
        routesMap = defaultdict(list) # stop : routes
        for r in range(len(routes)):
            for stop in routes[r]:
                routesMap[stop].append(r)

        # Step 2: put source stop into queue and bfs on its routes
        queue = deque([source])
        visitedStops = set([source])
        visitedRoutes = set()
        output = 0

        while queue:
            for _ in range(len(queue)):
                currStop = queue.popleft()
                if currStop == target:
                    return output

                for route in routesMap[currStop]:
                    if route not in visitedRoutes: # go through all stops in route
                        visitedRoutes.add(route)
                        
                        for stop in routes[route]:
                            if stop not in visitedStops:
                                visitedStops.add(stop)
                                queue.append(stop)
            output += 1
        return -1 # if we're here, means did not find target
