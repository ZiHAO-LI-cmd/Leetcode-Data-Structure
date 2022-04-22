# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root == None:
            return TreeNode(val)
        
        node = root
        while node:
            if val < node.val:  # 插在左子树
                if node.left == None:   # 原左子树为空，新建插入
                    node.left = TreeNode(val)
                    break
                else:
                    node = node.left    # 如果该子树不为空，则问题转化成了将val插入到对应子树上
            else:
                if node.right == None:
                    node.right = TreeNode(val)
                    break
                else:
                    node = node.right
        return root


# 递归
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root == None:
            return TreeNode(val)
        
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        
        return root