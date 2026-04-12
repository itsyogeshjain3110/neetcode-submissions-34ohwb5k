class Solution:
    def isValid(self, s: str) -> bool:
        help_dict = {")": "(", "}": "{", "]": "["}
        stack = []
        for i in s:
            if stack and i in ")]}":
                if stack[-1] != help_dict.get(i):
                    return False
                stack.pop()
            else:
                stack.append(i) 
        return len(stack) == 0

        