# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if root is None:
                return True, 0
            balanced_at_left, height_at_left = dfs(root.left)
            if not balanced_at_left:
                return False, 0
            balanced_at_right , height_at_right = dfs(root.right)
            if not balanced_at_right:
                return False, 0
            if abs(height_at_left - height_at_right) > 1:
                return False, 0
            return True, 1 + max(height_at_left , height_at_right)
        return dfs(root)[0]
        
        