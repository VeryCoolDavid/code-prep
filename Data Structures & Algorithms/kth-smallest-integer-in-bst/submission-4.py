# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, r: Optional[TreeNode], k: int) -> int:
        cnt=k
        res = r.val
        
        def root(node):
            nonlocal cnt, res
            if not node:
                return
            root(node.left)
            if cnt==0:
                return 
            cnt-=1
            if cnt==0:
                res=node.val
                return 
            root(node.right)
        root(r)
        return res