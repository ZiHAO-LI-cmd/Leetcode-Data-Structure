# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        from queue import Queue
        res = []
        tmp = []
        que = Queue()
        que.put(root)
        while not que.empty():
            for _ in range(que.qsize()):
                node = que.get()
                tmp.append(node.val)
                if node.left:
                    que.put(node.left)
                if node.right:
                    que.put(node.right)
            res.append(tmp)
            tmp = []
        return res

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
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
        return res

