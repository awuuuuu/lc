import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        hq = [float('-inf')] * k
        heapq.heapify(hq)
        for n in nums:
            if n > hq[0]:
                heapq.heappop(hq)
                heapq.heappush(hq, n)
        return hq[0]
        
  
  
import Queue
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pq = Queue.PriorityQueue()
        for n in nums:
            pq.put(n)
            if pq.qsize() > k:
            	pq.get()
        return pq.get()
