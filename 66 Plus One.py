while 循环跳出遗漏

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = len(digits)
        while i >= 0:
            i = i - 1
            if digits[i] == 9:
                digits[i] = 0
                if i == 0:
                    return [1] + digits
            else:
                digits[i] = digits[i] + 1
                break
        return digits
