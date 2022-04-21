# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False
        if root.left == None and root.right == None:    #叶子节点
            return targetSum == root.val
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)



# BFS
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False
        que = []
        que.insert(0, (root, root.val))
        
        while que:
            node, curSum = que.pop()
            # if curSum == targetSum:
            #     return True
            # 要到最后的叶子节点才能判断是否相等
            if node.left:
                que.insert(0, (node.left, curSum + node.left.val))
            if node.right:
                que.insert(0, (node.right, curSum + node.right.val))
            
            # 要到最后的叶子节点才能判断是否相等
            if node.left == None and node.right == None and curSum == targetSum:
                return True
        return False