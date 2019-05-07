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
        cur = res
        #cur 如果直接赋值为res.next则是None没有指针指向
        count = 0
        while l1 or l2 or count:
            count += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            cur.next = ListNode(count%10)
            cur = cur.next
            #这里的count计算要注意，不空空想
            count = 1 if count>9 else 0
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            if (l1 is None or l2 is None) and count == 0:
                cur.next = l2 if l2 else l1
                break
        return res.next       
