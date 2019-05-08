
#超时，DP，速度太慢
import operator

def get_key(i,j):
	return '-'.join((str(i), str(j)))

class NumArray:

    def __init__(self, nums: List[int]):
        m = {}
        for i in range(len(nums)):
            for j in range(i+1):
                if j < i:
                    m[get_key(j, i)] = operator.add(m[get_key(j, operator.sub(i,1))], nums[i])
                else:
                    m[get_key(j, i)] = nums[i]
        self.m = m

    def sumRange(self, i: int, j: int) -> int:
        return self.m[get_key(i,j)]




# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

#有时候不要死脑筋

import operator


class NumArray:

    def __init__(self, nums: List[int]):
        self.m = []
        if len(nums) == 0:
            return
        self.m = [nums[0]]
        for i in range(1, len(nums)):
            self.m.append(operator.add(nums[i], self.m[i-1]))

    def sumRange(self, i: int, j: int) -> int:
        if i >j or len(self.m) == 0:
            return 0
        if i > 0:
            return operator.sub(self.m[j], self.m[i-1])
        return self.m[j]
