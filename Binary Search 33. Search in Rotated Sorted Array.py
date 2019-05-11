# redo

class Solution:
    #4 5 6 7 8 9 10 0 1 2   
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        l = 0
        r = len(nums)-1
        while l<r:
            mid = int((r+l)/2)
            if nums[mid] >= nums[r]:
                l = mid + 1
            else:
                r = mid
        startIndex = l
        l = 0
        r = len(nums)-1
        while l<=r:
            mid = int((r+l)/2)
            realMid = (mid + startIndex)%len(nums)
            if nums[realMid] == target:
                return realMid
            elif nums[realMid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1
                
