# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # DFS
        if root == None:
            return 0
        leftHeight = self.maxDepth(root.left)
        rightHeight = self.maxDepth(root.right)
        return max(leftHeight, rightHeight) + 1


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 层序遍历
        if root == None:
            return 0
        res = []
        tmp = []
        que = []
        que.insert(0, root)
        while que:
            for _ in range(len(que)):
                node = que.pop()
                tmp.append(node.val)
                if node.left:
                    que.insert(0, node.left)
                if node.right:
                    que.insert(0, node.right)
            res.append(tmp)
            tmp = []
        return len(res)