# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 0
        max_so_far = float("-inf")
        def dfs(node, max_so_far):
            if node is None:
                return
            if node.val >= max_so_far:
                max_so_far = node.val
                self.ans+=1
            return dfs(node.left, max_so_far) or dfs(node.right, max_so_far)
            
        dfs(root, max_so_far)
        return self.ans
        