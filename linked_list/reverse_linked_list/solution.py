# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        if head is None:
           return head
        reverse_head = {"result": None}
        p = head
        self.reverseListHelper(p, reverse_head)
        return reverse_head["result"]

    def reverseListHelper(self, p, reverse_head):
        if p.next is None:
            reverse_head["result"] = p
            return
        self.reverseListHelper(p.next, reverse_head)
        q = p.next
        q.next = p
        p.next = None
