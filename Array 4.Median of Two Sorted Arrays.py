
#无限math.inf,取整int or math.floor,注意float和int

import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = []
        i = 0
        j = 0
        while i <len(nums1) or j < len(nums2):
            v1 = nums1[i] if i<len(nums1) else math.inf
            v2 = nums2[j] if j<len(nums2) else math.inf
            if v1 < v2:
                arr.append(v1)
                i = i + 1
            else:
                arr.append(v2)
                j = j + 1
        if len(arr) % 2 == 0:
            return (arr[int(len(arr)/2)] + arr[int(len(arr)/2) - 1])/2
        return arr[int(len(arr)/2)] * 1.0
