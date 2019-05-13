##wcnm 啊

import collections
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = dict(collections.Counter(t))
        i=I=0
        missing = len(t)
        J = 0

        for j,c in enumerate(s, 1):
            if c in count:
                if count[c] > 0:
                    missing -= 1
                count[c] -= 1
                if missing == 0:
                    while i < j and missing == 0:
                        if missing == 0:
                            if J== 0 or J-I > j-i:
                                I,J = i,j
                        if s[i] in count:
                            if count[s[i]] == 0:
                                missing += 1
                            count[s[i]] += 1
                        i += 1
        return s[I:J]
