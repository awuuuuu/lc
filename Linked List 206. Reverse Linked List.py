#注意第一行的判断head is None在前，不需重刷


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        new = None
        cur = head
        nex = head.next
        while nex.next:
            cur.next = new
            new = cur
            cur = nex
            nex = nex.next
        cur.next = new
        nex.next = cur
        return nex
            
