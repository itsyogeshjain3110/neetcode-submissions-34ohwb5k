class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i:[] for i in range(n)}

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = set()
        components = 0
        def dfs(node):
            if node in visited:
                return 
            
            visited.add(node)
            for neighbour in graph[node]:
                dfs(neighbour)

        for i in range(n):
            if i not in visited:
                dfs(i)
                components+=1
        return components
        