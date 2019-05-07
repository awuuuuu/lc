# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None or l2 is None:
            return l1 if l1 else l2
        res = ListNode(0)
        cur = res.next
        count = 0
        while l1 or l2 or count:
            count += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            cur = ListNode(count%10)
            cur = cur.next
            count = count - count%10
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            if (l1 is None or l2 is None) and count == 0:
                cur = l2 if l2 else l1
                break
        return res.next
                
            
