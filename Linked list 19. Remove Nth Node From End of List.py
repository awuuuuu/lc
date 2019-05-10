#链表一定要注意头部，一般都设置一个头部避免边界情况

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        h = ListNode(0)
        h.next = head
        cur = head
        prev = h
        e = cur
        for i in range(n):
            e = e.next
        if head.next is None:
            return e
        while e:
            prev = cur
            cur = cur.next
            e = e.next
        prev.next = cur.next
        return h.next
        
