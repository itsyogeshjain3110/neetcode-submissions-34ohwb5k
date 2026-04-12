class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {course:[] for course in range(numCourses)}
        # adjacency list crs , its related prerequisites
        for a,b in prerequisites:
            graph[a].append(b)

        # 0 -> unvisited
        # -1 -> currently visiting
        # 1 -> already visited

        def dfs(crs):
            # means visiting again
            if visited[crs] == -1:
                return False
            # already visited
            if visited[crs] == 1:
                return True

            #mark as currently visiting
            visited[crs] = -1

            for pre in graph[crs]:
                if not dfs(pre):
                    return False
    
            # means all pre are not having cycle
            visited[crs] = 1
            return True

        visited = [0] * numCourses 
        # 0 means unvisited
        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True

        