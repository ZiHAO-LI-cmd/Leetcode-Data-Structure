# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # 自顶向下
        # def recursion(root):
        #     if root == None:  #递归出口
        #         return
        #     root.left, root.right = root.right, root.left
        #     recursion(root.left)
        #     recursion(root.right)

        # recursion(root)
        # return root

        #自底向上
        if not root:
            return
        root.left , root.right = self.invertTree(root.right) , self.invertTree(root.left)
        return root

