# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # 中序遍历
        def DFS(node):
            if node == None:
                return
            DFS(node.left)
            res.append(node.val)
            DFS(node.right)

        res = []
        DFS(root)
        # for i in range(len(res)-1):
        #     for j in range(i+1, len(res)):
        #         if res[i] + res[j] == k:
        #             return True

        # return False

        left, right = 0, len(res) - 1
        while left < right:
            s = res[left] + res[right]
            if s == k:
                return True
            if s < k:
                left += 1
            else:
                right -= 1
        return False


# 深度优先搜索 + 哈希表
class Solution:
    def __init__(self):
        self.s = set()

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if root is None:
            return False
        if k - root.val in self.s:
            return True
        self.s.add(root.val)
        return self.findTarget(root.left, k) or self.findTarget(root.right, k)

