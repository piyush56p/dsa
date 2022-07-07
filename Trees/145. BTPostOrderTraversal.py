#------------------RECURSIVE--------------------
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        a=[]
        def dfs(root):
            if root:
                dfs(root.left)
                
                dfs(root.right)
                a.append(root.val)
            else:
                return
        dfs(root)
        return a
    
    #--------------------ITERATIVE--------------
    # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        stack =[root]
        while stack:
            n = len(stack)
            
            while n>0:
                node = stack.pop()
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
                res.append(node.val)
                n-=1
        res.sort(reverse=True)
        return res
