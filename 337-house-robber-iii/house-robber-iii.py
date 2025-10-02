# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo={} 
        def dp(root):
            if not root:
                return 0
            if root in memo:
                return memo[root]
            take= root.val
            if root.left:
                take+=dp(root.left.left) + dp(root.left.right)
            if root.right:
                take+=dp(root.right.left)+dp(root.right.right)

            notake=dp(root.left) + dp(root.right)
            memo[root]= max(take, notake)
            return memo[root]
        return dp(root)