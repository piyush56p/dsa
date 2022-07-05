# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        def maxdepth(root):
            
            if root:
                
                leftheight = maxdepth(root.left)
                rightheight = maxdepth(root.right)
                self.diameter = max(self.diameter, leftheight+rightheight)
                return 1+max(leftheight,rightheight)
            else:
                return 0
        maxdepth(root)
        return self.diameter
