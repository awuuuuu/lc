#以为很简单，结果还是错了好几次

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        arr = []
        stack = [[root]]
        while len(stack):
            t = stack.pop()
            a = []
            b = []
            for i in t:
                b.append(i.val)
                if i.left:
                    a.append(i.left)
                if i.right:
                    a.append(i.right)
            if len(a):
                stack.append(a)
            if len(b):
                arr.append(b)
        return arr
