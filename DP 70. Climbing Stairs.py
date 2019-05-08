
#新增数组元素用append！！！，index注意
import operator
class Solution:
    def climbStairs(self, n: int) -> int:
        a = [1,2]
        for i in range(2,n):
            a.append(operator.add(a[i-1], a[i-2]))
        return a[n-1]
