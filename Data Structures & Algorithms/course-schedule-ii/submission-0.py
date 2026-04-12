class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {crs:[] for crs in range(numCourses)}
        for a,b in prerequisites:
            graph[a].append(b)

        output = []

        def dfs(crs):
            if visited[crs] == -1:
                return False
            if visited[crs] == 1:
                return True

            visited[crs] = -1
            for pre in graph[crs]:
                if not dfs(pre):
                    return []

            output.append(crs)
            visited[crs] = 1
            return True


        visited = [0] * numCourses
        for crs in range(numCourses):
            if visited[crs] == 0:
                if not dfs(crs):
                    return []
        return output
        