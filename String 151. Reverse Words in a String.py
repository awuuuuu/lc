

import re
class Solution:
    def reverseWords(self, s: str) -> str:
        arr = list(filter(lambda x: x, re.split(r"\s*", s)))
        i = 0
        j = len(arr)-1
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        return " ".join(arr)
