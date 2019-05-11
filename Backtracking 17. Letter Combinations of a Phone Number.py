#重做
#第一版本

m = {
    "2": ['a', 'b', 'c'],
    "3": ['d', 'e', 'f'],
    "4": ['g', 'h', 'i'],
    "5": ['j', 'k', 'l'],
    "6": ['m', 'n', 'o'],
    "7": ['p', 'q', 'r', 's'],
    "8": ['t', 'u', 'v'],
    "9": ['w', 'x', 'y', 'z']
}
def get(arr, s):
    if s == "":
        return
    l = len(arr)
    dl = len(m[s[0]])
    s_arr = m[s[0]]
    for j in range(dl):
        for i in range(l):
            if j != dl-1:
                arr.append(arr[i] + s_arr[j+1])
            else:
                arr[i] = arr[i] + s_arr[0]
    get(arr, s[1::])

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        arr = [i for i in m[digits[0]]]
        get(arr, digits[1::])
        
        return arr


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        arr = [''] if digits else []
        m = [0, 1, 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        for i in digits:
            arr = [s+v for s in arr for v in m[int(i)]]
        return arr
