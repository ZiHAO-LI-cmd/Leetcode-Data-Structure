# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # 中序遍历
        def DFS(node):
            if node == None:
                return
            DFS(node.left)
            res.append(node.val)
            DFS(node.right)

        res = []
        DFS(root)
        # tmp = res.sort() .sort()没有返回值
        tmp = sorted(res)
        if (tmp == res) and (len(res) == len(set(res))):    #中序遍历的结果递增且没有重复值
            return True
        else:
            return False