class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT, window = {}, {}

        for i in t:
            countT[i] = 1 + countT.get(i,0)

        have, need = 0 , len(countT)
        res , resLen = [-1,-1], float("inf")
        l = 0
        for r in range(len(s)):
            ch = s[r]
            window[ch] = 1 + window.get(ch, 0)

            if ch in countT and window[ch] == countT[ch]:
                have+=1

            while have == need:
                if (r-l+1) < resLen:
                    resLen = r-l+1
                    res = [l,r]
                
                window[s[l]]-=1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have-=1
                l+=1
        l,r = res
        return s[l:r+1] if resLen != float("inf") else ""


        