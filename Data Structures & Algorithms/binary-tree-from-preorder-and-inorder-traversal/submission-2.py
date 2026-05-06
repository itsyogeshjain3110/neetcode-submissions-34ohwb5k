# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:],inorder[mid+1:])
        return root
    # def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    #     inorder_map = {val:i for i,val in enumerate(inorder)}
    #     self.pre_index = 0
    #     def dfs(left,right):
    #         if left > right:
    #             return

    #         root_val = preorder[self.pre_index]
    #         self.pre_index+=1

    #         root = TreeNode(root_val)
    #         mid = inorder_map[root_val]
    #         root.left = dfs(left, mid-1)
    #         root.right = dfs(mid+1,right)
    #         return root
    #     return dfs(0,len(preorder)-1)

        