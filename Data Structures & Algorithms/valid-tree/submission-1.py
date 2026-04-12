class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False

        # Step 1: Build adjacency list
        graph = {i:[] for i in range(n)}
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u) # because its a uni-directed graph

        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False

            visited.add(node)
            # check for neighbours
            for neighbour in graph[node]:
                if neighbour == parent:
                    continue # Skip the edge back to the parent
                if not dfs(neighbour,node):
                    return False # Found cycle deeper down

            return True

        if not dfs(0,-1):
            return False

        return len(visited) == n
        