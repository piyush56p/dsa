#--------------------RECURSIVE-------------------
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        a=[]
        def dfs(root):
            if root:
                dfs(root.left)
                a.append(root.val)
                dfs(root.right)
            else:
                return
        dfs(root)
        return a
    
    #-----------------------ITERATIVE-----------------
    # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        current = root
        stack = []
        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            elif(stack):
                current = stack.pop()
                res.append(current.val)
                current = current.right
            else:
                break
        return res
