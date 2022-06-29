# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        arr = [-1,0,1]
        def height(root):
            if not root:
                return -1;
            else:
                lh = height(root.left)
               
                rh = height(root.right)
                return max(lh,rh) +1
        def dfsbalance(root):
            if not root:
                return True
            else:
                if(abs(height(root.left) - height(root.right)) < 2) and     dfsbalance(root.right) and dfsbalance(root.left):
                    return True
                else:
                    return False
                
        return dfsbalance(root)
