class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = { c:set() for w in words for c in w}

        for i in range(len(words)-1):
            # taking pair by pair
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            # if one word is a prefix of the other but comes later, it's invalid
            #abc,ab here ab should have come before abc
            if w1[:minLen] == w2[:minLen] and len(w1) > len(w2):
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        # adj like  t->f , f->r
        visited = {} # 0 = unvisited, -1 = visiting, 1 = visited
        res = []

        #DFS post order
        def dfs(char):
            if char in visited:
                return visited[char] == 1  # Return True only if fully visited
            
            visited[char] = -1 #visiting
            
            for neighChar in adj[char]:
                if not dfs(neighChar): #cycle detected in neigh
                    return False

            visited[char] = 1
            #post order
            res.append(char)
            return True




        for char in adj:
            if char not in visited:
                if not dfs(char): # means cycle detected
                    return ""

        return "".join(res[::-1])

        
            


        