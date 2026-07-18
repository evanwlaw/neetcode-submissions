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
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        # populate routes map
        routesMap = defaultdict(list)
        for route in range(len(routes)):
            for stop in routes[route]:
                routesMap[stop].append(route)

        queue = deque([source])
        visitedStop = set([source])
        visitedRoute = set()
        output = 0

        while queue:
            for i in range(len(queue)):
                currStop = queue.popleft()
                if currStop == target:
                    return output 
                
                # go through routes of current stop and then check each stop in route 
                for route in routesMap[currStop]:
                    if route not in visitedRoute:
                        visitedRoute.add(route)
                        for stop in routes[route]:
                            if stop not in visitedStop:
                                visitedStop.add(stop)
                                queue.append(stop)
            output += 1
                    
        return -1 
