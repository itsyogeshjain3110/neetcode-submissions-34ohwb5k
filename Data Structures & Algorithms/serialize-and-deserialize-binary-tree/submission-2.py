# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        serialized_str = []
        def preorder(node):
            if not node:
                serialized_str.append("null")    
                return
            serialized_str.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        return "&".join(serialized_str)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # data -> 1&2&null&null&3&4&null&null&5&null&null
        if not data:
            return
        data = data.split("&")
        def build(preorder_iter):
            val = next(preorder_iter)
            if val == "null":
                return None
            root = TreeNode(int(val))
            root.left = build(preorder_iter)
            root.right = build(preorder_iter)
            return root

            
        return build(iter(data))
        
