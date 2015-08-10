# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {boolean}
    def isPalindrome(self, head):
        tmp = []
        while head is not None:
            tmp.append(head.val)
            head = head.next

        length = len(tmp)
        for i in range(length/2):
            if tmp[i] != tmp[length-1-i]:
                return False
        return True

