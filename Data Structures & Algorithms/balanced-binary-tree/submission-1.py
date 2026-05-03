# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def height(self,root):
        if root is None:
            return 0
        return 1 + max(self.height(root.left),self.height(root.right))
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if root is None:
            return True
        height_at_left = self.height(root.left)
        height_at_right = self.height(root.right)
        if max(height_at_left,height_at_right) > 1 + min(height_at_left,height_at_right):
            return False
        return  self.isBalanced(root.left) and self.isBalanced(root.right) 
        
        