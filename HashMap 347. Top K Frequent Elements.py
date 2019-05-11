#queue不是Queue
#还行挺简单的，不用重做也行
from queue import PriorityQueue as PQ
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}
        for i in nums:
            if i in m:
                m[i] += 1
            else:
                m[i] = 1
        p = PQ()
        for key in m.keys():
            p.put((-m[key], key))
        res = []
        for i in range(k):
            res.append(p.get()[1])
        return res
