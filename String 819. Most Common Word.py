# 无需重做，记住字符串lower, upper, re.split即可

import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        s_list = re.split(r"\s|\!|\?|\'|\,|\;|\.", paragraph.lower())
        b_m = {}
        p_m = {}
        for i in banned:
            b_m[i] = 1
        count = 0
        key = ""
        for i in s_list:
            if i and i not in b_m:
                if i in p_m:
                    p_m[i] = p_m[i] + 1
                else:
                    p_m[i] = 1
                if p_m[i] > count:
                    count = p_m[i]
                    key = i    
        return key
