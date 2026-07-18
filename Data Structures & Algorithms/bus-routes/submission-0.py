from collections import defaultdict, deque

class Solution:
    '''

    BFS each through each route to find the target.
    Each BFS layer is number of buses

    routesMap = {stop : [r0, r1,...]}

    Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
    Output: 2

    1 : r0
    2 : r0
    7 : r0, r1
    3 : r1
    6 : r1

    
    bfs through each route
        if current stop is target, return number of buses/routes taken
        loop through all routes in routesMap[currentStop]

    return -1
    '''
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        routesMap = defaultdict(list) # stop : routeNumber
        # populate routes map
        for i, route in enumerate(routes):
            for stop in route:
                routesMap[stop].append(i)

        queue = deque([source])
        visitedStops = set([source])
        visitedRoutes = set()

        output = 0
        while queue:
            for i in range(len(queue)):
                currStop = queue.popleft()
                if currStop == target:
                    return output

                for route in routesMap[currStop]:
                    if route not in visitedRoutes:
                        for stop in routes[route]:
                            if stop not in visitedStops:
                                visitedStops.add(stop)
                                queue.append(stop)
                        visitedRoutes.add(route)
            output += 1
        return -1


