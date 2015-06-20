# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} sum
    # @return {boolean}
    def hasPathSum(self, root, sum):
        if root is None:
            return False
        if root.left is None and root.right is None:
            return root.val == sum
        if self.hasPathSum(root.left, sum-root.val):
            return True
        if self.hasPathSum(root.right, sum-root.val):
            return True
        return False

