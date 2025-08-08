from collections import deque
def solution(tickets):
    answer = []
    tickets.sort()
    # visited = [False] * len(tickets)
    # first = []
    cities = []
    def dfs(a , visited, route):
        if len(route) == len(tickets)+1:
            cities.append(route)
            return 
        for t in range(len(tickets)):
            if tickets[t][0] == a and not visited[t] :
                visited[t] = True
                dfs(tickets[t][1] , visited, route + [tickets[t][1]])
                visited[t] = False
    visited = [False] * len(tickets)
    dfs("ICN" , visited, ["ICN"])
    return cities[0]
