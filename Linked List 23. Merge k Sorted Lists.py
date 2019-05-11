#sort 函数使用，for i in lists:, i 是item不是index
#TODO 用from Queue import PriorityQueue

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return None
        if (len(lists)) == 1:
            return lists[0]
        new_lists = []
        for i in lists:
            if i:
                new_lists.append(i)
        new_lists.sort(key=lambda x:x.val)
        head = ListNode(0)
        c = head
        listIndex = 0
        while listIndex < len(new_lists):
            c.next = new_lists[listIndex]
            c = c.next
            new_lists[listIndex] = new_lists[listIndex].next
            if new_lists[listIndex] is None:
                listIndex += 1
            else:
                t = listIndex
                for i in range(listIndex+1, len(new_lists)):
                    if new_lists[t].val < new_lists[i].val:
                        break
                    else:
                        new_lists[t], new_lists[i] = new_lists[i], new_lists[t]
                        t = i
        return head.next
        
#貌似这个慢。。
        
 class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return None
        if (len(lists)) == 1:
            return lists[0]
        from Queue import PriorityQueue as PQ
        q = PQ()
        for i in lists:
            if i:
                q.put((i.val, i))
        head = ListNode(0)
        cur = head
        while q.qsize() > 0:
            t = q.get()[1]
            cur.next = t
            if t.next:
                q.put((t.next.val, t.next))
            cur = cur.next
        return head.next
        
