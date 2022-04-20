# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True

        def dfs(left, right):
            if (not left) and (not right):  # 两个值都为空
                return True
            if (not left) or (not right):  # 有一个值为空
                return False
            if left.val != right.val:
                return False
            return dfs(left.left, right.right) and dfs(left.right, right.left)

        return dfs(root.left, root.right)


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True

        que = []
        que.insert(0, root.left)
        que.insert(0, root.right)
        while que:
            node1 = que.pop()
            node2 = que.pop()
            if (not node1) and (not node2):  # 如果两个节点都为空
                continue
            if (not node1) or (not node2):
                return False
            if node1.val != node2.val:
                return False
            que.append(node1.left)
            que.append(node2.right)
            que.append(node1.right)
            que.append(node2.left)

        return True
