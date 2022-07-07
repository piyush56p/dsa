# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        if root:
            q=deque([root])

            while q:
                level = []

                n = len(q)
                while n>0:
                    node = q.popleft()
                    n -= 1
                    level.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                if level:
                    res.append(level)
        
                
        
        return res
        
