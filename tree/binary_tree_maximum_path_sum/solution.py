# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def maxPathSum(self, root):
        max_sum = []
        max_sum.append("start")
        self.caculateSum(root, max_sum)
        return max_sum[0]

    def caculateSum(self, root, max_sum):
        if root is None:
            return 0
        left_sum = self.caculateSum(root.left, max_sum)
        right_sum = self.caculateSum(root.right, max_sum)
        current = max(root.val, root.val+left_sum, root.val+right_sum)
        accross_root_sum = root.val + left_sum + right_sum
        if max_sum[0] == "start":
            max_sum[0] = max(current, accross_root_sum)
        else:
            max_sum[0] = max(current, accross_root_sum, max_sum[0])
        return current
