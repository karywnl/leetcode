class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_sort = strs.copy()
        res = []

        for i in range(len(strs)):
            lst = list(strs[i])
            lst.sort()
            strs_sort[i] = "".join(lst)
    
    
        for i in range(len(strs_sort)):
            if strs[i] == None:
                continue
            res_temp = []
            for j in range(i, len(strs_sort)):
                if strs_sort[i] == strs_sort[j]:
                    res_temp.append(strs[j])
                    strs[j] = None
            res.append(res_temp)

        return res