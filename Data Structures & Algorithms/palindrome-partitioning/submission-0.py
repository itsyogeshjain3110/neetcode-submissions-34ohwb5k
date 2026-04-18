class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []

        def is_palindrome(sub):
            return sub == sub[::-1]

        def backtrack(start ,curr):
            if start == len(s):
                ans.append(curr[:])
                return

            for end in range(start+1, len(s)+1):
                part = s[start:end]
                if not is_palindrome(part):
                    continue

                #make choice
                curr.append(part)

                backtrack(end,curr)

                # undo
                curr.pop()

        backtrack(0, [])

        return ans
        