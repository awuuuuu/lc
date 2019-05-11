class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new_strs = []
        for i in strs:
        #################
            new_strs.append("".join(sorted(i)))
        m = {}
        for i in range(len(strs)):
            if new_strs[i] in m:
                m[new_strs[i]].append(strs[i])
            else:
                m[new_strs[i]] = [strs[i]]
        return list(m.values())
