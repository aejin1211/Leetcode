class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        route = []
        for a, b in sorted(tickets):
            graph[a].append(b)
        
        def dfs(departure):
            while graph[departure]:
                dfs(graph[departure].pop(0))
            route.append(departure)
        dfs('JFK')
        return route[::-1]