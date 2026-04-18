class Solution:
    def letterCombinations(self, digits: str) -> List[str]: 
        keypad = {"2": "abc", "3": "def","4": "ghi", "5": "jkl", "6":"mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        ans = []
        if not digits:
            return ans

        def backtrack(start, path):
            if start == len(digits):
                ans.append("".join(path))
                return
            
            digit = digits[start]
            for ch in keypad[digit]:
                path.append(ch)
                backtrack(start+1, path)
                path.pop()

        backtrack(0,[])

        return ans
    
