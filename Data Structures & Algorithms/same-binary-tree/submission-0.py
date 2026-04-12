# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        check_left_of_both = self.isSameTree(p.left,q.left)
        check_right_of_both = self.isSameTree(p.right,q.right)
        if check_left_of_both and check_right_of_both and p.val == q.val:
            return True
        else:
            return False
        