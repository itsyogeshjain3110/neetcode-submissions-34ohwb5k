class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count = {}
        max_f = 0
        output = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r],0)
            max_f = max(max_f, count[s[r]])
            while (r-l+1)-max_f > k:
                count[s[l]]-=1
                l+=1
            output = max(output, r-l+1)

        return output
        