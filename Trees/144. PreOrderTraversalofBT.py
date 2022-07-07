#--------------------------RECURSIVE---------------------
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        a=[]
        def dfs(root):
            if root:
                a.append(root.val)
                dfs(root.left)
                dfs(root.right)
            else:
                return
        dfs(root)
        return a
    
    #-----------------------ITERATIVE----------------------
    # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        if root:
            stack = [root]
            while stack:
                n = len(stack)
                while n>0:
                    node = stack.pop()
                    n-=1
                    res.append(node.val)
                    if node.right:
                        stack.append(node.right)
                    if node.left:
                        stack.append(node.left)
        return res
