# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def DFS(node):
            if node == None:
                return
            
            DFS(node.left)
            res.append(node.val)
            DFS(node.right)

        res = []
        DFS(root)
        return res