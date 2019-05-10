# 重做

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        cur = head
        
        while cur:
            newNode = Node(cur.val,cur.next, cur.random)
            nex = cur.next
            cur.next = newNode
            cur = nex
        
        cur = head
        while cur:
            newNode = cur.next
            if newNode.random:
                newNode.random = newNode.random.next
            cur = newNode.next
        
        cur = head
        c = Node(0,None,None)
        newCur = c
        while cur:
            newCur.next = cur.next
            cur.next = cur.next.next
            cur = cur.next
            newCur = newCur.next
        return c.next
        
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head is None:
            return None
        cur = head
        m = {}
        while cur:
            newNode = Node(cur.val, None, None)
            m[cur] = newNode
            cur = cur.next
        
        cur = head
        c = m[cur]
        newCur = c
        while cur:
            if cur.next:
                newCur.next = m[cur.next]
            if cur.random:
                newCur.random = m[cur.random]
            newCur = newCur.next
            cur = cur.next
        return c
