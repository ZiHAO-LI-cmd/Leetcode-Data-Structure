# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        que = []
        que.insert(0, root)
        while que:
            node = que.pop()
            if node.val == val:
                return node
                # res = []
                # tmpQue = [node]
                # while tmpQue:
                #     tmp = tmpQue.pop()
                #     res.append(tmp)
                #     if tmp.left:
                #         tmpQue.insert(0, tmp.left)
                #     if tmp.right:
                #         tmpQue.insert(0, tmp.right)
                # return res
            if node.left:
                que.insert(0, node.left)
            if node.right:
                que.insert(0, node.right)
        return None


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:

        if root == None:
            return
        if root.val == val:
            return root
        if root.val > val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)
