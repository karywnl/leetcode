class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cnt_s = {}
        cnt_t = {}

        for x in s:
            if x in cnt_s:
                cnt_s[x] += 1
            else:
                cnt_s[x] = 1
        
        for x in t:
            if x in cnt_t:
                cnt_t[x] += 1
            else:
                cnt_t[x] = 1
            
        if cnt_t == cnt_s:
            return True
        return False