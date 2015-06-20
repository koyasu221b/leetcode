# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} sum
    # @return {integer[][]}
    def pathSum(self, root, sum):
        output = []
        if root is None:
            return []
        tmp = []
        self.pathSumHelper(root, sum, tmp, output)
        return output

    def pathSumHelper(self, root, sum, tmp, output):
        if root is None:
            return
        tmp.append(root.val)
        if root.left is None and root.right is None:
            if root.val == sum:
                _tmp = list(tmp)
                output.append(_tmp)
                return
        if root.left is not None:
            self.pathSumHelper(root.left, sum-root.val, tmp, output)
            tmp.pop()
        if root.right is not None:
            self.pathSumHelper(root.right, sum-root.val, tmp, output)
            tmp.pop()
        return
