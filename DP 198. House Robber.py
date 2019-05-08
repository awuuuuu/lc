#还行马马虎虎过了
import operator

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        a = [nums[0], max(nums[0], nums[1])]
        if len(nums) >= 3:
            a.append(max(operator.add(a[0], nums[2]), a[1])) 
            for i in range(3, len(nums)):
                a.append(
                    max(
                        operator.add(nums[i], a[i-3]),
                        operator.add(nums[i], a[i-2]),
                        #这里出了错
                        a[i-1]
                    )
                )
        return a[operator.sub(len(a), 1)]   
