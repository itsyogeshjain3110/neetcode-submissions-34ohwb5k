class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l=r=0
        hashmap = {}
        res = 1
        while r < len(s):
            if s[r] in hashmap:
                l = max(hashmap.get(s[r]) + 1,l)
            hashmap[s[r]] = r
            print(l,r,res)
            res = max(res,r-l+1)
            r+=1
        return res



        